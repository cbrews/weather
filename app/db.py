from contextlib import contextmanager
from functools import lru_cache
from typing import Generator

from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from app.settings import settings


@lru_cache
def get_engine() -> Engine:
    config = settings()
    connection_str = f"postgresql+psycopg://{config.postgres_user}:{config.postgres_password}@{config.postgres_host}:{config.postgres_port}/{config.postgres_database}"
    return create_engine(connection_str)


@contextmanager
def session() -> Generator[Session, None, None]:
    """
    Basic wrapper for session so we don't have to directly
    use the engine in service code
    """
    yield Session(get_engine())


def session_fastapi_dependency() -> Generator[Session, None, None]:
    """
    Session wrapped as a dependency for use by FastAPI
    """
    with session() as s:
        yield s


def drop_all() -> None:
    """
    Clear out schema
    """
    SQLModel.metadata.drop_all(get_engine())


def migrate() -> None:
    """
    Create database based on models.

    In the real world we would use migration files but this works for a toy system.
    """
    SQLModel.metadata.create_all(get_engine())
