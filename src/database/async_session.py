import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

user = os.getenv("PSQL_DB_USERNAME")
password = os.getenv("PSQL_DB_PASSWORD")
localhost = os.getenv("PSQL_DB_HOST")
dbname = os.getenv("PSQL_DB_DATABASE_NAME")
port = os.getenv("PSQL_DB_PORT")

Base = declarative_base()

DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{localhost}:{port}/{dbname}"
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_db(session: AsyncSession):
    async with session.begin():
        await session.run_sync(Base.metadata.create_all)


async def close_db(session: AsyncSession):
    await session.close()