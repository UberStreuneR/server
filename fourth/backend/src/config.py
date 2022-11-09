from pydantic import BaseSettings, PostgresDsn
from os import getenv


class Settings(BaseSettings):
    database_url: PostgresDsn = "postgresql://postgres:mypassword@localhost:2345/bank_api"


def get_settings() -> Settings:
    settings = Settings()
    if (db := getenv("POSTGRES_DB")) is not None:
        settings.database_url = PostgresDsn.build(
            scheme="postgresql",
            user=settings.database_url.user,
            password=settings.database_url.password,
            host=settings.database_url.host,
            port=settings.database_url.port,
            path=f"/{db}",
        )
    return settings
