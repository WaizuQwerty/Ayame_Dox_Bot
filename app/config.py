
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_API_TOKEN: str
    PROBIVAPI_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
