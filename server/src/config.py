from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

ENV_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = ENV_DIR / ".env"

class Settings(BaseSettings):
    DB_PASS : str
    DB_NAME : str
    DB_PORT : int
    DB_HOST : str
    DB_USER : str


    def URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    model_config = SettingsConfigDict(env_file=ENV_FILE)

settings = Settings()
