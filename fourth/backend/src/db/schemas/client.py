from pydantic import BaseModel
from typing import Any, List
from .account import AccountSchema


class ClientSchema(BaseModel):
    client_id: Any
    name: str
    accounts: List[AccountSchema]

    class Config:
        orm_mode = True


class ClientCreate(BaseModel):
    name: str


class ClientUpdate(ClientCreate):
    pass
