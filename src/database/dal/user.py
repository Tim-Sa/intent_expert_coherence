from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

import src.database.model.user as db_model
import src.model.user as py_model

import src.database.dal.abs_crud as crud


async def create_user(
    db: AsyncSession,
    user: py_model.UserCreate
) -> py_model.UserRead:
    return await crud.create_instance(db, db_model.User, user.model_dump(), py_model.UserRead)


async def get_user(
    db: AsyncSession,
    user_id: int
) -> Optional[py_model.UserRead]:
    return await crud.get_instance(db, db_model.user, user_id, 'id')


async def get_all_users(
    db: AsyncSession
) -> List[py_model.UserRead]:
    return await crud.get_all_instances(db, db_model.user)


async def update_user(
    db: AsyncSession,
    user_id: int,
    user_update: py_model.UserUpdate
) -> Optional[py_model.UserRead]:
    return await crud.update_instance(
        db, db_model.user, user_id, 'id', user_update.model_dump(exclude_unset=True)
    )


async def delete_user(
    db: AsyncSession,
    user_id: int
) -> bool:
    return await crud.delete_instance(db, db_model.user, user_id, 'id')

