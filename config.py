# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GEMINI_KEY: str
    GEMINI_MODEL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
