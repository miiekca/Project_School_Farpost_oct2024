from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engine = create_async_engine(settings.DB_URL)

async_session_maker = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass