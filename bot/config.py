
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    BOT_TOKEN : str
    ACCESS_USER_IDS: list[int]
    
settings = Settings()