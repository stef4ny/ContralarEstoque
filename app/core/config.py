import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EMAIL_HOST: str
    EMAIL_PORT: int = 587
    EMAIL_USER: str
    EMAIL_PASSWORD: str
    EMAIL_TO: str

    class Config:
        env_file = ".env"

settings = Settings()
