from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

import src.database.model.entity as db_model
import src.model.entity as py_model

import src.database.dal.abs_crud as crud


async def create_text_intent(
    db: AsyncSession,
    text_intent: py_model.TextIntentCreate
) -> py_model.TextIntentRead:
    return await crud.create_instance(
        db, db_model.TextIntent, text_intent.model_dump(), py_model.TextIntentRead
    )


async def get_text_intent(
    db: AsyncSession,
    text_intent_id: int
) -> Optional[py_model.TextIntentRead]:
    return await crud.get_instance(db, db_model.TextIntent, text_intent_id, 'text_intent_id')


async def get_all_text_intents(
    db: AsyncSession
) -> List[py_model.TextIntentRead]:
    return await crud.get_all_instances(db, db_model.TextIntent)


async def update_text_intent(
    db: AsyncSession,
    text_intent_id: int,
    text_intent_update: py_model.TextIntentUpdate
) -> Optional[py_model.TextIntentRead]:
    return await crud.update_instance(
        db, db_model.TextIntent, text_intent_id, 'text_intent_id', text_intent_update.model_dump(exclude_unset=True)
    )


async def delete_text_intent(
    db: AsyncSession,
    text_intent_id: int
) -> bool:
    return await crud.delete_instance(db, db_model.TextIntent, text_intent_id, 'text_intent_id')


async def create_expert(
    db: AsyncSession,
    expert: py_model.ExpertCreate
) -> py_model.ExpertRead:
    return await crud.create_instance(db, db_model.Expert, expert.model_dump(), py_model.ExpertRead)


async def get_expert(
    db: AsyncSession,
    expert_id: int
) -> Optional[py_model.ExpertRead]:
    return await crud.get_instance(db, db_model.Expert, expert_id, 'expert_id')


async def get_all_experts(
    db: AsyncSession
) -> List[py_model.ExpertRead]:
    return await crud.get_all_instances(db, db_model.Expert)


async def update_expert(
    db: AsyncSession,
    expert_id: int,
    expert_update: py_model.ExpertCreate
) -> Optional[py_model.ExpertRead]:
    return await crud.update_instance(
        db, db_model.Expert, expert_id, 'expert_id', expert_update.model_dump(exclude_unset=True)
    )


async def delete_expert(
    db: AsyncSession,
    expert_id: int
) -> bool:
    return await crud.delete_instance(db, db_model.Expert, expert_id, 'expert_id')


async def create_intent_type(
    db: AsyncSession,
    intent_type: py_model.IntentTypeCreate
) -> py_model.IntentTypeRead:
    return await crud.create_instance(db, db_model.IntentType, intent_type.model_dump(), py_model.IntentTypeRead)


async def get_intent_type(
    db: AsyncSession,
    intent_type_id: int
) -> Optional[py_model.IntentTypeRead]:
    return await crud.get_instance(db, db_model.IntentType, intent_type_id, 'type_id')


async def get_all_intent_types(
    db: AsyncSession
) -> List[py_model.IntentTypeRead]:
    return await crud.get_all_instances(db, db_model.IntentType)


async def update_intent_type(
    db: AsyncSession,
    intent_type_id: int,
    intent_type_update: py_model.IntentTypeUpdate
) -> Optional[py_model.IntentTypeRead]:
    return await crud.update_instance(
        db, db_model.IntentType, intent_type_id, 'type_id', intent_type_update.model_dump(exclude_unset=True)
    )


async def delete_intent_type(
    db: AsyncSession,
    intent_type_id: int
) -> bool:
    return await crud.delete_instance(db, db_model.IntentType, intent_type_id, 'type_id')


async def create_intent(
    db: AsyncSession,
    intent: py_model.IntentCreate
) -> py_model.IntentRead:
    return await crud.create_instance(db, db_model.Intent, intent.model_dump(), py_model.IntentRead)


async def get_intent(
    db: AsyncSession,
    intent_id: int
) -> Optional[py_model.IntentRead]:
    return await crud.get_instance(db, db_model.Intent, intent_id, 'intent_id')


async def get_all_intents(
    db: AsyncSession
) -> List[py_model.IntentRead]:
    return await crud.get_all_instances(db, db_model.Intent)


async def update_intent(
    db: AsyncSession,
    intent_id: int,
    intent_update: py_model.IntentUpdate
) -> Optional[py_model.IntentRead]:
    return await crud.update_instance(
        db, db_model.Intent, intent_id, 'intent_id', intent_update.model_dump(exclude_unset=True)
    )


async def delete_intent(
    db: AsyncSession,
    intent_id: int
) -> bool:
    return await crud.delete_instance(db, db_model.Intent, intent_id, 'intent_id')
