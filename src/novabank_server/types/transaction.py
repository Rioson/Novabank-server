# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bank_account import BankAccount

__all__ = ["Transaction"]


class Transaction(BaseModel):
    id: int

    amount: float

    created_at: str

    source_account: BankAccount

    status: str

    transaction_type: str

    provider: Optional[str] = None

    target_bank_account_number: Optional[str] = None

    target_bank_name: Optional[str] = None

    target_country: Optional[str] = None

    target_iban: Optional[str] = None

    target_phone_number: Optional[str] = None

    target_swift_code: Optional[str] = None
