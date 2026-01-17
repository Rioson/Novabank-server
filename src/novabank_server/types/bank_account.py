# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .bank_server import BankServer

__all__ = ["BankAccount"]


class BankAccount(BaseModel):
    id: int

    account_name: str

    account_number: str

    bank_server: BankServer
