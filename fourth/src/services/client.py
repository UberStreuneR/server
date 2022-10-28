from .base import BaseService
from src.db.models import Client
from src.db.schemas.client import ClientCreate, ClientUpdate
from sqlalchemy.orm import Session


class ClientService(BaseService[Client, ClientCreate, ClientUpdate]):
    def __init__(self, session: Session) -> None:
        super().__init__(Client, session)
