from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import OperationalError
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

async def create_engine(db_url):
    async_engine = create_async_engine(db_url, echo=True, future=True, dialect="postgresql+asyncpg")
    async with async_engine.connect() as conn:
        await conn.execute("SELECT 1")
    return async_engine

try:
    DB_URL = os.getenv("DATABASE_URL")
    DB_URL = DB_URL.replace("postgres://", "postgresql://")


except (OperationalError, KeyError):
    DB_URL = os.getenv("DATABASE_URL")
    

async def get_session():
    engine = await create_engine(DB_URL)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

Base = declarative_base()
if __name__ == "__main__":
    asyncio.run(get_session())