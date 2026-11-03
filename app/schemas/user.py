from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    # для ответа пользователю из ORM
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr
    is_active: bool


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AccessToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
