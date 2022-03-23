from typing import Optional
from pydantic import BaseSettings, Field
from functools import lru_cache
from dotenv import load_dotenv


class Settings(BaseSettings):
    env: str = Field(None, env="ENV")
    db: Optional[str] = None
    admin_email: Optional[str] = None
    admin_password: Optional[str] = None

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


@lru_cache()
def get_settings():
    load_dotenv()
    return DevSettings() if Settings().env == 'dev' else ProdSettings()
