from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mounting the static directory for CSS and other assets
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setting up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate(num1: float, num2: float, operation: str):
    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = num1 / num2
    else:
        return {"error": "Invalid operation"}

    return {"result": result}
