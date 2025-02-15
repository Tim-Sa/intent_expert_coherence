from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional

import model as db_model
import model.model as py_model


async def create_text_intent(
    db: AsyncSession, 
    text_intent: py_model.TextIntentCreate
) -> py_model.TextIntentRead:
    
    db_text_intent = db_model.TextIntent(**text_intent.dict())
    db.add(db_text_intent)
    
    await db.commit()
    await db.refresh(db_text_intent)
    
    return py_model.TextIntentRead.from_orm(db_text_intent)


async def get_text_intent(
    db: AsyncSession, 
    text_intent_id: int
) -> Optional[py_model.TextIntentRead]:
    
    result = await db.execute(
        select(db_model.TextIntent).filter(db_model.TextIntent.text_intent_id == text_intent_id)
    )
    
    return result.scalars().first()


async def get_all_text_intents(
    db: AsyncSession
) -> List[py_model.TextIntentRead]:
    
    result = await db.execute(select(db_model.TextIntent))
    return result.scalars().all()


async def update_text_intent(
    db: AsyncSession,
    text_intent_id: int,
    text_intent_update: py_model.TextIntentUpdate
) -> Optional[py_model.TextIntentRead]:
    
    stmt = (
        update(db_model.TextIntent)
        .where(db_model.TextIntent.text_intent_id == text_intent_id)
        .values(**text_intent_update.dict(exclude_unset=True))
    )
    
    await db.execute(stmt)
    await db.commit()
    
    return await get_text_intent(db, text_intent_id)


async def delete_text_intent(
    db: AsyncSession,
    text_intent_id: int
) -> bool:
    
    stmt = delete(db_model.TextIntent).where(db_model.TextIntent.text_intent_id == text_intent_id)
    result = await db.execute(stmt)
    await db.commit()
    
    return result.rowcount > 0  # Return True if a row was deleted
