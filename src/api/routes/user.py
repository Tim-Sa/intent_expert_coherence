from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel
from typing import List, Optional

from src.database.async_session import AsyncSessionLocal
import src.database.model.user as db_model # sqlalchemy models
import src.model.user as py_model  # Pydantic models
import src.database.dal.user as dal 

from src.auth.hash_password import HashPassword
from src.auth.jwt_handler import verify_access_token

from src.api.utils import get_db

user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")

hash_password = HashPassword()


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access"
        )

    decoded_token = verify_access_token(token)
    
    return decoded_token["user"]


@user_router.post(
    "/user/signin", 
    response_model=py_model.Token, 
    tags=["Users"], 
    status_code=status.HTTP_201_CREATED
)
async def create_user_endpoint(
    user: py_model.UserWrite,
    db: AsyncSession = Depends(get_db),
):

    hashed_password = hash_password.create_hash(user.password)
    new_user = py_model.UserCreate(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password 
    )

    return await dal.create_user(db, new_user)