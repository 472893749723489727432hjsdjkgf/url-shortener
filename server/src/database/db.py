from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from server.src.config import settings
from pydantic import BaseModel

engine = create_async_engine(url=settings.URL())

session = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

