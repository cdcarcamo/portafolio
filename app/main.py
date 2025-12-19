# Proyecto de portafolio personal

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers.views import router as views_router

app = FastAPI(title="Cárcamo System Company")

# Servir carpeta static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(views_router)

