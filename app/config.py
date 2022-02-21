from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    env: str = Field(None, env="ENV")
    db: Optional[str] = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class DevSettings(Settings):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"


class ProdSettings(Settings):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"
