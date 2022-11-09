from .base import BaseService
from src.db.schemas.account import AccountCreate
from src.db.models import Account
from sqlalchemy.orm import Session


class AccountService(BaseService[Account, AccountCreate, None]):
    def __init__(self, session: Session) -> None:
        super().__init__(Account, session)

