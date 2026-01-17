# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .bank_account import BankAccount

__all__ = ["BankAccountListResponse"]

BankAccountListResponse: TypeAlias = List[BankAccount]
