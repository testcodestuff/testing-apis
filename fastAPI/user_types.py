from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    url: str = "not found"
    id: int


class AuthUser(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class DBUser(AuthUser):
    password: str
