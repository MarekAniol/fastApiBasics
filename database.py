from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    