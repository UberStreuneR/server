from pydantic import BaseModel
from typing import List
from .line import LineSchema


class AccountSchema(BaseModel):
    account_id: int
    client_id: int
    lines: List[LineSchema]

    class Config:
        orm_mode = True


class AccountCreate(BaseModel):
    client_id: int
