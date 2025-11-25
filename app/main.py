# Proyecto de portafolio personal

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Servir carpeta static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Servir carpeta template
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})