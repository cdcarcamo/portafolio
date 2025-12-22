# Proyecto de portafolio personal

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.routers.views import router as views_router
from pathlib import Path


    

app = FastAPI(title="Cárcamo System Company")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(views_router)

