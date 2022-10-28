from http.client import HTTPException
from typing import List, TypeVar, Generic, Type, Any, Optional
import sqlalchemy
from sqlalchemy.orm import Session
from src.db.models import Base
from src.db.schemas.client import ClientCreate, ClientUpdate
from fastapi import HTTPException
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
SchemaCreateType = TypeVar("SchemaCreateType", bound=BaseModel)
SchemaUpdateType = TypeVar("SchemaUpdateType", bound=BaseModel)


class BaseService(Generic[ModelType, SchemaCreateType, SchemaUpdateType]):
    def __init__(self, model: Type[ModelType], session: Session) -> None:

        self.model = model
        self.session = session

    def get(self, id: Any) -> Optional[ModelType]:
        obj = self.session.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not found")
        return obj

    def list(self) -> List[ModelType]:
        arr = self.session.query(self.model).all()
        return arr

    def post(self, obj: SchemaCreateType) -> ModelType:
        db_obj = self.model(**obj.dict())
        self.session.add(db_obj)
        try:
            self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_obj

    def update(self, id: Any, obj: SchemaUpdateType) -> ModelType:
        db_obj = self.get(id)
        for column, value in obj.dict(exclude_unset=True).items():
            setattr(db_obj, column, value)
        self.session.commit()
        return db_obj

    def delete(self, id: Any) -> None:
        db_obj = self.get(id)
        self.session.delete(db_obj)
        self.session.commit()
