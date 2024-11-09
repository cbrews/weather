from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_database: str


@lru_cache
def settings() -> Settings:
    """
    Instantiates the settings from the environment.
    Note that this is cached after initially called.
    """
    return Settings()
