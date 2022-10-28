from pydantic import BaseModel
from typing import Any, List


class LineSchema(BaseModel):
    line_id: int
    account_id: int
    credit_sum: int

    class Config:
        orm_mode = True


class LineCreate(BaseModel):
    account_id: int
    credit_sum: int
