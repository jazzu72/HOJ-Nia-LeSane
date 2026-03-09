from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    FOUNDER_PAUSE_PASSWORD: str = "AddieMaeLeSane33"
    OWNER_EMAIL: str = "lesane1972@gmail.com"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
