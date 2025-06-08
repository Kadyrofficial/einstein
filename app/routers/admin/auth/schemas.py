from pydantic import BaseModel, EmailStr, Field


class LoginSchema(BaseModel):
    email: EmailStr
    password:str = Field(min_length=8, max_length=16)


class TokenSchema(BaseModel):
    token: str

