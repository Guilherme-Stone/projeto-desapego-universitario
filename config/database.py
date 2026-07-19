import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

class Base(DeclarativeBase):
    pass

class Database:
    def __init__(self):
        database_url = "postgresql+asyncpg://postgres:123456@localhost:5432/meu_banco"

        self.engine = create_async_engine(
            database_url,
            echo=True,
            pool_pre_ping=True,
        )

        self.session_maker = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_db(self):
        async with self.session_maker() as session:
            yield session


db = Database()