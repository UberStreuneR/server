from typing import Any, List
from fastapi import APIRouter, Depends, status
from src.services import get_line_service
from src.services.line import LineService
from src.db.schemas.line import LineSchema, LineCreate

router = APIRouter(tags=["line"], prefix="/lines")


@router.get("/{line_id}", response_model=LineSchema)
def get_line(line_id: Any, line_service: LineService = Depends(get_line_service)):
    return line_service.get(line_id)


@router.get("/", response_model=List[LineSchema])
def get_lines(line_service: LineService = Depends(get_line_service)):
    return line_service.list()


@router.post("/", response_model=LineSchema, status_code=status.HTTP_201_CREATED)
def add_line(line: LineCreate, line_service: LineService = Depends(get_line_service)):
    return line_service.post(line)


@router.delete("/{line_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_line(line_id: int, line_service: LineService = Depends(get_line_service)):
    return line_service.delete(line_id)
