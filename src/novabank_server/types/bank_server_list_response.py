# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .bank_server import BankServer

__all__ = ["BankServerListResponse"]

BankServerListResponse: TypeAlias = List[BankServer]
