from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.config import get_settings

engine = create_engine(get_settings().database_url)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session