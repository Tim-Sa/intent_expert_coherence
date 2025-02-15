from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy Base
Base = declarative_base()

# Create an async engine
DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{localhost}/{dbname}"
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session
