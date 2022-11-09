from fastapi import Depends

from .account import AccountService
from .client import ClientService
from .line import LineService
from src.db.session import get_session


def get_client_service(session=Depends(get_session)) -> ClientService:
    return ClientService(session)


def get_account_service(session=Depends(get_session)) -> AccountService:
    return AccountService(session)


def get_line_service(session=Depends(get_session)) -> LineService:
    return LineService(session)


__all__ = ['get_client_service', 'get_account_service', 'get_line_service']
