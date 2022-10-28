from typing import Any, List
from fastapi import APIRouter, Depends, status
from src.services import get_account_service
from src.services.account import AccountService
from src.db.schemas.account import AccountSchema, AccountCreate

router = APIRouter(tags=["account"], prefix="/accounts")


@router.get("/{account_id}", response_model=AccountSchema)
def get_account(account_id: Any, account_service: AccountService = Depends(get_account_service)):
    return account_service.get(account_id)


@router.get("/", response_model=List[AccountSchema])
def get_accounts(account_service: AccountService = Depends(get_account_service)):
    return account_service.list()


@router.post("/", response_model=AccountSchema, status_code=status.HTTP_201_CREATED)
def add_account(account: AccountCreate, account_service: AccountService = Depends(get_account_service)):
    return account_service.post(account)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(account_id: int, account_service: AccountService = Depends(get_account_service)):
    return account_service.delete(account_id)
