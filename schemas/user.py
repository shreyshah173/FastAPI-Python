from pydantic import BaseModel, EmailStr


class UserSignup(BaseModel):
    fullname: str
    email: EmailStr
    username: str
    password: str
    age: int


class UserLogin(BaseModel):
    username: str
    password: str
