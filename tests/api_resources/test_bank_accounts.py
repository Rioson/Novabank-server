# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from novabank_server import NovabankServer, AsyncNovabankServer
from novabank_server.types import (
    BankAccount,
    BankAccountListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBankAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: NovabankServer) -> None:
        bank_account = client.bank_accounts.create(
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: NovabankServer) -> None:
        response = client.bank_accounts.with_raw_response.create(
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: NovabankServer) -> None:
        with client.bank_accounts.with_streaming_response.create(
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NovabankServer) -> None:
        bank_account = client.bank_accounts.retrieve(
            0,
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NovabankServer) -> None:
        response = client.bank_accounts.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NovabankServer) -> None:
        with client.bank_accounts.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: NovabankServer) -> None:
        bank_account = client.bank_accounts.update(
            account_id=0,
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: NovabankServer) -> None:
        response = client.bank_accounts.with_raw_response.update(
            account_id=0,
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: NovabankServer) -> None:
        with client.bank_accounts.with_streaming_response.update(
            account_id=0,
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: NovabankServer) -> None:
        bank_account = client.bank_accounts.list()
        assert_matches_type(BankAccountListResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: NovabankServer) -> None:
        response = client.bank_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccountListResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: NovabankServer) -> None:
        with client.bank_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccountListResponse, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: NovabankServer) -> None:
        bank_account = client.bank_accounts.delete(
            0,
        )
        assert bank_account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: NovabankServer) -> None:
        response = client.bank_accounts.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert bank_account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: NovabankServer) -> None:
        with client.bank_accounts.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert bank_account is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBankAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNovabankServer) -> None:
        bank_account = await async_client.bank_accounts.create(
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_accounts.with_raw_response.create(
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_accounts.with_streaming_response.create(
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNovabankServer) -> None:
        bank_account = await async_client.bank_accounts.retrieve(
            0,
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_accounts.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_accounts.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNovabankServer) -> None:
        bank_account = await async_client.bank_accounts.update(
            account_id=0,
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_accounts.with_raw_response.update(
            account_id=0,
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_accounts.with_streaming_response.update(
            account_id=0,
            account_name="account_name",
            account_number="account_number",
            bank_server=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNovabankServer) -> None:
        bank_account = await async_client.bank_accounts.list()
        assert_matches_type(BankAccountListResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccountListResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccountListResponse, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNovabankServer) -> None:
        bank_account = await async_client.bank_accounts.delete(
            0,
        )
        assert bank_account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_accounts.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert bank_account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_accounts.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert bank_account is None

        assert cast(Any, response.is_closed) is True
