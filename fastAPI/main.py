from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="dog")


@app.get("/")
async def root():
    return "Some text"


@app.get("/url")
async def url():
    return {"url": "google.com"}
