from fastapi import APIRouter, HTTPException, status
from variables import list_of_users
from user_types import User

router = APIRouter(tags=["Users"])


@router.get("/users")
async def users():
    return list_of_users


@router.get("/user/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user(id: int):
    # Async to keep code consistency
    return await search_user(id)


@router.post("/user/", response_model=User, status_code=status.HTTP_200_OK)
async def post_user(user: User) -> User:
    searched_user = await search_user(user.id)
    if isinstance(searched_user, User):
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="User already exists"
        )

    list_of_users.append(user)
    return user


@router.put("/user/", response_model=User, status_code=status.HTTP_201_CREATED)
async def put_user(user: User) -> User:
    new_user = User(name="Name6", surname="surname6", id=6)
    found = False
    for i, saved_user in enumerate(list_of_users):
        if saved_user.id != user.id:
            continue
        list_of_users[i] = new_user
        found = True

    if not found:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return new_user


@router.delete(
    "/user/{id}", response_model=str, status_code=status.HTTP_200_OK
)
async def delete_user(id: int):
    found = False
    for i, saved_user in enumerate(list_of_users):
        if saved_user.id != id:
            continue
        del list_of_users[i]
        found = True

    if not found:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


async def search_user(id: int) -> User:
    user_with_id = filter(lambda user: user.id == id, list_of_users)

    if not user_with_id:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user_with_id
