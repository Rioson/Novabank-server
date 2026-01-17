# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BankAccountUpdateParams"]


class BankAccountUpdateParams(TypedDict, total=False):
    account_name: Required[str]

    account_number: Required[str]

    bank_server: Required[int]
