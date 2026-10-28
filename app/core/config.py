from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

dir_settings = Path(__file__).resolve().parent.parent.parent
# print(f"Settings file . env path {dir_settings}")


class SettingsApp(BaseSettings):
    # если отсутствует env, то использовать эти настройки
    PROJECT_NAME: str = "shop-app"
    API_V1_PREFIX: str = "/api/v1"
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/shop.db"
    # SECRET_KEY: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool = False
    # для настроек приложения чеез .env
    model_config = SettingsConfigDict(
        env_file=dir_settings / ".env",
        env_file_encoding="utf-8",
    )


settings = SettingsApp()

if __name__ == "__main__":
    print("---SettingsAPP---")
    print(settings.model_dump())
