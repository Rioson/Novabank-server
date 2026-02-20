# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from novabank_server import NovabankServer, AsyncNovabankServer
from novabank_server.types import (
    BankServer,
    BankServerListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBankServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: NovabankServer) -> None:
        bank_server = client.bank_servers.create(
            id=0,
            name="name",
        )
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: NovabankServer) -> None:
        response = client.bank_servers.with_raw_response.create(
            id=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = response.parse()
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: NovabankServer) -> None:
        with client.bank_servers.with_streaming_response.create(
            id=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = response.parse()
            assert_matches_type(BankServer, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NovabankServer) -> None:
        bank_server = client.bank_servers.retrieve(
            0,
        )
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NovabankServer) -> None:
        response = client.bank_servers.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = response.parse()
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NovabankServer) -> None:
        with client.bank_servers.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = response.parse()
            assert_matches_type(BankServer, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: NovabankServer) -> None:
        bank_server = client.bank_servers.update(
            server_id=0,
            id=0,
            name="name",
        )
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: NovabankServer) -> None:
        response = client.bank_servers.with_raw_response.update(
            server_id=0,
            id=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = response.parse()
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: NovabankServer) -> None:
        with client.bank_servers.with_streaming_response.update(
            server_id=0,
            id=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = response.parse()
            assert_matches_type(BankServer, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: NovabankServer) -> None:
        bank_server = client.bank_servers.list()
        assert_matches_type(BankServerListResponse, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: NovabankServer) -> None:
        response = client.bank_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = response.parse()
        assert_matches_type(BankServerListResponse, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: NovabankServer) -> None:
        with client.bank_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = response.parse()
            assert_matches_type(BankServerListResponse, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: NovabankServer) -> None:
        bank_server = client.bank_servers.delete(
            0,
        )
        assert bank_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: NovabankServer) -> None:
        response = client.bank_servers.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = response.parse()
        assert bank_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: NovabankServer) -> None:
        with client.bank_servers.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = response.parse()
            assert bank_server is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBankServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNovabankServer) -> None:
        bank_server = await async_client.bank_servers.create(
            id=0,
            name="name",
        )
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_servers.with_raw_response.create(
            id=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = await response.parse()
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_servers.with_streaming_response.create(
            id=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = await response.parse()
            assert_matches_type(BankServer, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNovabankServer) -> None:
        bank_server = await async_client.bank_servers.retrieve(
            0,
        )
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_servers.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = await response.parse()
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_servers.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = await response.parse()
            assert_matches_type(BankServer, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNovabankServer) -> None:
        bank_server = await async_client.bank_servers.update(
            server_id=0,
            id=0,
            name="name",
        )
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_servers.with_raw_response.update(
            server_id=0,
            id=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = await response.parse()
        assert_matches_type(BankServer, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_servers.with_streaming_response.update(
            server_id=0,
            id=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = await response.parse()
            assert_matches_type(BankServer, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNovabankServer) -> None:
        bank_server = await async_client.bank_servers.list()
        assert_matches_type(BankServerListResponse, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = await response.parse()
        assert_matches_type(BankServerListResponse, bank_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = await response.parse()
            assert_matches_type(BankServerListResponse, bank_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNovabankServer) -> None:
        bank_server = await async_client.bank_servers.delete(
            0,
        )
        assert bank_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNovabankServer) -> None:
        response = await async_client.bank_servers.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_server = await response.parse()
        assert bank_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNovabankServer) -> None:
        async with async_client.bank_servers.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_server = await response.parse()
            assert bank_server is None

        assert cast(Any, response.is_closed) is True
