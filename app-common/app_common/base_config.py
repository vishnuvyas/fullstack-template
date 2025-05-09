from pydantc_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os

ENV = os.getenv("ENV", "")


class BaseConfig(BaseSettings):
    db_url: str = Field(
        default="sqlite+aiosqlite:///:memory:",
        description="sqlalchemy compatible async database url"
    )
    debug: bool = Field(
        default=False,
        description="Enables debug logging at various levels"
    )
    model_config = SettingsConfigDict(env_file=f"{ENV}.env")
