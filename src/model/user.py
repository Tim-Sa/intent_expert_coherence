from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr


class UserWrite(UserBase):
    password: constr(min_length=6)


class UserCreate(UserBase):
    hashed_password: constr(min_length=6)


class UserUpdate(UserBase):
    hashed_password: Optional[constr(min_length=6)] = None


class UserAuth(BaseModel):
    username: str
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserRead(UserBase):
    id: int
    created_at: datetime  
    updated_at: datetime  

    class Config:
        from_attributes=True
