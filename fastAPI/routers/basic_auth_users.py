from typing import Optional
from variables import users_db
from user_types import AuthUser, DBUser
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(tags=["basicauth"])


router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


async def search_user_db(username: str) -> Optional[DBUser]:
    if username in users_db:
        return DBUser(**users_db[username])

    return None


async def search_user(username: str) -> Optional[AuthUser]:
    if username in users_db:
        return AuthUser(**users_db[username])

    return None


async def current_user(token: str = Depends(oauth2)) -> AuthUser:
    user = await search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Auth Credentials",
        )

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Disabled User"
        )

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_in_db = users_db.get(form.username, {})

    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not registered",
        )

    user = await search_user_db(form.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Auth Credentials",
        )

    if form.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )

    # TODO Create encrypted access_token
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: AuthUser = Depends(current_user)):
    return user
