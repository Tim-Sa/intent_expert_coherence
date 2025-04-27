from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.orm import declarative_base
from typing import List, Optional
from pydantic import BaseModel

Base = declarative_base()


async def create_instance(
    db: AsyncSession,
    model: Base,
    instance_data: dict,
    read_model: BaseModel
) -> BaseModel:
    async with db.begin():
        db_instance = model(**instance_data)
        db.add(db_instance)
        await db.flush()
        await db.refresh(db_instance)
    return read_model.model_validate(db_instance)


async def get_instance(
    db: AsyncSession,
    model: Base,
    instance_id: int,
    instance_id_column: str
) -> Optional[BaseModel]:
    async with db.begin():
        result = await db.execute(
            select(model).filter(getattr(model, instance_id_column) == instance_id)
        )
    return result.scalars().first()


async def get_all_instances(
    db: AsyncSession,
    model: Base
) -> List[BaseModel]:
    async with db.begin():
        result = await db.execute(select(model))
    return result.scalars().all()


async def update_instance(
    db: AsyncSession,
    model: Base,
    instance_id: int,
    instance_id_column: str,
    update_data: dict
) -> Optional[BaseModel]:
    async with db.begin():
        stmt = (
            update(model)
            .where(getattr(model, instance_id_column) == instance_id)
            .values(**update_data)
        )
        await db.execute(stmt)
        await db.flush()

    return await get_instance(db, model, instance_id, instance_id_column)


async def delete_instance(
    db: AsyncSession,
    model: Base,
    instance_id: int,
    instance_id_column: str
) -> bool:
    async with db.begin():
        stmt = delete(model).where(getattr(model, instance_id_column) == instance_id)
        result = await db.execute(stmt)
        await db.flush()

    return result.rowcount > 0