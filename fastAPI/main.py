from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    url: str = "not found"
    id: int


list_of_users = [User(name="Name1", surname="surname1", id=1),
                 User(name="Name2", surname="surname2", id=2),
                 User(name="Name3", surname="surname3", id=3)]


@app.get("/users")
async def users():
    return list_of_users


@app.get("/user/{id}")
async def user(id: int):
    return await search_user(id)


async def search_user(id: int):
    users = filter(lambda user: user.id == id, list_of_users)

    try:
        return list(users)[0]
    except Exception:
        return {"error": "User not found"}
