from sqlalchemy.ext.asyncio import AsyncSession
from src.database.async_session import AsyncSessionLocal

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()