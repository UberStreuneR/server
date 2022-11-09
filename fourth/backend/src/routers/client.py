from typing import Any, List
from fastapi import APIRouter, Depends, status
from src.services import get_client_service
from src.services.client import ClientService
from src.db.schemas.client import ClientCreate, ClientUpdate, ClientSchema

router = APIRouter(tags=["client"], prefix="/clients")


@router.get("/{client_id}", response_model=ClientSchema)
def get_client(client_id: Any, client_service: ClientService = Depends(get_client_service)):
    return client_service.get(client_id)


@router.get("/", response_model=List[ClientSchema])
def get_clients(client_service: ClientService = Depends(get_client_service)):
    return client_service.list()


@router.post("/", response_model=ClientSchema)
def add_client(client: ClientCreate, client_service: ClientService = Depends(get_client_service)):
    return client_service.post(client)


@router.patch("/{client_id}", response_model=ClientSchema)
def update_client(client_id: Any, client: ClientUpdate, client_service: ClientService = Depends(get_client_service)):
    return client_service.update(client_id, client)


@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: Any, client_service: ClientService = Depends(get_client_service)):
    return client_service.delete(client_id)
