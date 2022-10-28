from .base import BaseService
from src.db.models import LineOfCredit
from src.db.schemas.line import LineCreate
from sqlalchemy.orm import Session


class LineService(BaseService[LineOfCredit, LineCreate, None]):
    def __init__(self, session: Session) -> None:
        super().__init__(LineOfCredit, session)
