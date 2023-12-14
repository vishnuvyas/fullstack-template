from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
BASE_PATH = "/api/v2"
api = FastAPI()
api.mount(
    "/static", StaticFiles(directory='static', html=True), name='static')


@api.get("/health")
def health() -> str:
    return "healthy!"
