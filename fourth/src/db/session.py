from sqlalchemy import create_engine
from src.config import get_settings

engine = create_engine(get_settings().database_url)
