from fastapi import FastAPI, Depends, HTTPException, status, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel
from typing import List, Optional

from src.database.async_session import AsyncSessionLocal

import src.database.model as db_model # sqlalchemy schemas
import src.model.model as py_model  # Pydantic models

from src.database.dal import create_expert, get_expert, get_all_experts, update_expert, delete_expert

app = FastAPI(title="Expert API")
router = APIRouter()


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/experts/", response_model=py_model.ExpertRead, tags=["Experts"])
async def create_expert_endpoint(
    expert: py_model.ExpertCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_expert(db, expert)


@router.get("/experts/{expert_id}", response_model=py_model.ExpertRead, tags=["Experts"])
async def get_expert_endpoint(
    expert_id: int,
    db: AsyncSession = Depends(get_db),
):
    expert = await get_expert(db, expert_id)
    if not expert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return expert


@router.get("/experts/", response_model=List[py_model.ExpertRead], tags=["Experts"])
async def get_all_experts_endpoint(
    db: AsyncSession = Depends(get_db),
):
    return await get_all_experts(db)


@router.put("/experts/{expert_id}", response_model=py_model.ExpertRead, tags=["Experts"])
async def update_expert_endpoint(
    expert_id: int,
    expert_update: py_model.ExpertCreate,
    db: AsyncSession = Depends(get_db),
):
    updated_expert = await update_expert(db, expert_id, expert_update)
    if not updated_expert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return updated_expert


@router.delete("/experts/{expert_id}", response_model=dict, tags=["Experts"])
async def delete_expert_endpoint(
    expert_id: int,
    db: AsyncSession = Depends(get_db),
):
    success = await delete_expert(db, expert_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return {"detail": "Expert deleted successfully"}


app.include_router(router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
