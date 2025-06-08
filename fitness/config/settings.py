from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class LogSettings(BaseModel):
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class Settings(BaseSettings):
    log: LogSettings = LogSettings()

    model_config = SettingsConfigDict(env_nested_delimiter="_")
