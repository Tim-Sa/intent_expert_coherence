from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional

import src.database.model as db_model
import src.model.model as py_model


async def create_instance(
    db: AsyncSession,
    model: db_model.Base,  # Use the base model type for flexibility
    instance_data: dict,
    read_model: py_model.BaseModel  # Use a general base type for Pydantic
) -> py_model.BaseModel :
    db_instance = model(**instance_data)
    db.add(db_instance)
    
    await db.commit()
    await db.refresh(db_instance)

    return read_model.from_orm(db_instance)


async def get_instance(
    db: AsyncSession,
    model: db_model.Base,
    instance_id: int,
    instance_id_column: str
) -> Optional[py_model.BaseModel]:
    result = await db.execute(
        select(model).filter(getattr(model, instance_id_column) == instance_id)
    )
    
    return result.scalars().first()


async def get_all_instances(
    db: AsyncSession,
    model: db_model.Base
) -> List[py_model.BaseModel]:
    result = await db.execute(select(model))
    return result.scalars().all()


async def update_instance(
    db: AsyncSession,
    model: db_model.Base,
    instance_id: int,
    instance_id_column: str,
    update_data: dict
) -> Optional[py_model.BaseModel]:
    stmt = (
        update(model)
        .where(getattr(model, instance_id_column) == instance_id)
        .values(**update_data)
    )
    await db.execute(stmt)
    await db.commit()

    return await get_instance(db, model, instance_id, instance_id_column)


async def delete_instance(
    db: AsyncSession,
    model: db_model.Base,
    instance_id: int,
    instance_id_column: str
) -> bool:
    stmt = delete(model).where(getattr(model, instance_id_column) == instance_id)
    result = await db.execute(stmt)
    await db.commit()
    return result.rowcount > 0  # Return True if a row was deleted


# Specific CRUD functions for TextIntent
async def create_text_intent(
    db: AsyncSession, 
    text_intent: py_model.TextIntentCreate
) -> py_model.TextIntentRead:
    return await create_instance(
        db, db_model.TextIntent, text_intent.dict(), py_model.TextIntentRead
    )


async def get_text_intent(
    db: AsyncSession, 
    text_intent_id: int
) -> Optional[py_model.TextIntentRead]:
    return await get_instance(db, db_model.TextIntent, text_intent_id, 'text_intent_id')


async def get_all_text_intents(
    db: AsyncSession
) -> List[py_model.TextIntentRead]:
    return await get_all_instances(db, db_model.TextIntent)


async def update_text_intent(
    db: AsyncSession,
    text_intent_id: int,
    text_intent_update: py_model.TextIntentUpdate
) -> Optional[py_model.TextIntentRead]:
    return await update_instance(
        db, db_model.TextIntent, text_intent_id, 'text_intent_id', text_intent_update.dict(exclude_unset=True)
    )


async def delete_text_intent(
    db: AsyncSession,
    text_intent_id: int
) -> bool:
    return await delete_instance(db, db_model.TextIntent, text_intent_id, 'text_intent_id')


# Specific CRUD functions for Expert
async def create_expert(
    db: AsyncSession, 
    expert: py_model.ExpertCreate
) -> py_model.ExpertRead:
    return await create_instance(db, db_model.Expert, expert.dict(), py_model.ExpertRead)


async def get_expert(
    db: AsyncSession, 
    expert_id: int
) -> Optional[py_model.ExpertRead]:
    return await get_instance(db, db_model.Expert, expert_id, 'expert_id')


async def get_all_experts(
    db: AsyncSession
) -> List[py_model.ExpertRead]:
    return await get_all_instances(db, db_model.Expert)


async def update_expert(
    db: AsyncSession,
    expert_id: int,
    expert_update: py_model.ExpertCreate
) -> Optional[py_model.ExpertRead]:
    return await update_instance(
        db, db_model.Expert, expert_id, 'expert_id', expert_update.dict(exclude_unset=True)
    )


async def delete_expert(
    db: AsyncSession,
    expert_id: int
) -> bool:
    return await delete_instance(db, db_model.Expert, expert_id, 'expert_id')
