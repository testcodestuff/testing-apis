from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["Users"])


class User(BaseModel):
    name: str
    surname: str
    url: str = "not found"
    id: int


list_of_users = [User(name="Name1", surname="surname1", id=1),
                 User(name="Name2", surname="surname2", id=2),
                 User(name="Name3", surname="surname3", id=3)]


@router.get("/users")
async def users():
    return list_of_users


@router.get("/user/{id}", response_model=User, status_code=200)
async def get_user(id: int):
    # Async to keep code consistency
    return await search_user(id)


@router.post("/user/", response_model=User, status_code=201)
async def post_user(user: User):
    if type(await search_user(user.id)) == User:
        return HTTPException(status_code=204, detail="User already exists")

    list_of_users.append(user)
    return user


@router.put("/user/", response_model=User, status_code=201)
async def put_user(user: User):
    new_user = User(name="Name6", surname="surname6", id=6)
    found = False
    for i, saved_user in enumerate(list_of_users):
        if saved_user.id != user.id:
            continue
        list_of_users[i] = new_user
        found = True

    if not found:
        return HTTPException(status_code=404, detail="User not found")

    return new_user


@router.delete("/user/{id}", response_model=str, status_code=200)
async def delete_user(id: int):
    found = False
    for i, saved_user in enumerate(list_of_users):
        if saved_user.id != id:
            continue
        del list_of_users[i]
        found = True

    if not found:
        return HTTPException(status_code=404, detail="User not found")


async def search_user(id: int):
    users = filter(lambda user: user.id == id, list_of_users)

    try:
        return list(users)[0]
    except Exception:
        return HTTPException(status_code=404, detail="User not found")
