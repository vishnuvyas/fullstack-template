from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

api = FastAPI()
api.mount("/static", StaticFiles(directory="static"), name='static')


@api.get("/health")
def health() -> str:
    return "healthy!"
