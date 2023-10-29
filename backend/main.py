from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

app.mount('/', StaticFiles(directory='dist', html=True))
