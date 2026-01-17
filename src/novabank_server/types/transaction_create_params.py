# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TransactionCreateParams"]


class TransactionCreateParams(TypedDict, total=False):
    amount: Required[float]

    source_account: Required[int]

    transaction_type: Required[str]

    provider: Optional[str]

    target_bank_account_number: Optional[str]

    target_bank_name: Optional[str]

    target_country: Optional[str]

    target_iban: Optional[str]

    target_phone_number: Optional[str]

    target_swift_code: Optional[str]
