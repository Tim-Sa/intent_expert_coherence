from fastapi import FastAPI, Depends, HTTPException, status, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel
from typing import List, Optional

from src.database.async_session import AsyncSessionLocal

import src.database.model as db_model # sqlalchemy models
import src.model.model as py_model  # Pydantic models

import src.database.dal as dal 

app = FastAPI(title="Expert API")
expert_router = APIRouter()
intent_type_router = APIRouter()


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()


@expert_router.post("/experts/", response_model=py_model.ExpertRead, tags=["Experts"], status_code=status.HTTP_201_CREATED)
async def create_expert_endpoint(
    expert: py_model.ExpertCreate,
    db: AsyncSession = Depends(get_db),
):
    return await dal.create_expert(db, expert)


@expert_router.get("/experts/{expert_id}", response_model=py_model.ExpertRead, tags=["Experts"])
async def get_expert_endpoint(
    expert_id: int,
    db: AsyncSession = Depends(get_db),
):
    expert = await dal.get_expert(db, expert_id)
    if not expert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return expert


@expert_router.get("/experts/", response_model=List[py_model.ExpertRead], tags=["Experts"])
async def get_all_experts_endpoint(
    db: AsyncSession = Depends(get_db),
):
    return await dal.get_all_experts(db)


@expert_router.put("/experts/{expert_id}", response_model=py_model.ExpertRead, tags=["Experts"])
async def update_expert_endpoint(
    expert_id: int,
    expert_update: py_model.ExpertCreate,
    db: AsyncSession = Depends(get_db),
):
    updated_expert = await dal.update_expert(db, expert_id, expert_update)
    if not updated_expert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return updated_expert


@expert_router.delete("/experts/{expert_id}", response_model=dict, tags=["Experts"])
async def delete_expert_endpoint(
    expert_id: int,
    db: AsyncSession = Depends(get_db),
):
    success = await dal.delete_expert(db, expert_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return {"detail": "Expert deleted successfully"}


@intent_type_router.post("/intent-types/", response_model=py_model.IntentTypeRead, tags=["Intent Types"], status_code=status.HTTP_201_CREATED)
async def create_intent_type_endpoint(
    intent_type: py_model.IntentTypeCreate,
    db: AsyncSession = Depends(get_db),
):
    return await dal.create_intent_type(db, intent_type)


@intent_type_router.get("/intent-types/{intent_type_id}", response_model=py_model.IntentTypeRead, tags=["Intent Types"])
async def get_intent_type_endpoint(
    intent_type_id: int,
    db: AsyncSession = Depends(get_db),
):
    intent_type = await dal.get_intent_type(db, intent_type_id)
    if not intent_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Intent Type not found")
    return intent_type


@intent_type_router.get("/intent-types/", response_model=List[py_model.IntentTypeRead], tags=["Intent Types"])
async def get_all_intent_types_endpoint(
    db: AsyncSession = Depends(get_db),
):
    return await dal.get_all_intent_types(db)


@intent_type_router.put("/intent-types/{intent_type_id}", response_model=py_model.IntentTypeRead, tags=["Intent Types"])
async def update_intent_type_endpoint(
    intent_type_id: int,
    intent_type_update: py_model.IntentTypeUpdate,
    db: AsyncSession = Depends(get_db),
):
    updated_intent_type = await dal.update_intent_type(db, intent_type_id, intent_type_update)
    if not updated_intent_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Intent Type not found")
    return updated_intent_type


@intent_type_router.delete("/intent-types/{intent_type_id}", response_model=dict, tags=["Intent Types"])
async def delete_intent_type_endpoint(
    intent_type_id: int,
    db: AsyncSession = Depends(get_db),
):
    success = await dal.delete_intent_type(db, intent_type_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Intent Type not found")
    return {"detail": "Intent Type deleted successfully"}


app.include_router(expert_router)
app.include_router(intent_type_router)

