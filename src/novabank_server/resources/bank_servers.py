# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bank_server_create_params, bank_server_update_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.bank_server import BankServer
from ..types.bank_server_list_response import BankServerListResponse

__all__ = ["BankServersResource", "AsyncBankServersResource"]


class BankServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BankServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#accessing-raw-response-data-eg-headers
        """
        return BankServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BankServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#with_streaming_response
        """
        return BankServersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: int,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServer:
        """
        Create a new bank server.

        Add a new bank server to the system with the provided details.

        Args: payload (BankServerSchema): Details of the new bank server.

        Returns: BankServerSchema: Details of the created bank server.

        Example Request:

        ```json
        {
          "name": "New Bank Server",
          "server_ip_address": "192.168.1.102"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "name": "New Bank Server",
          "server_ip_address": "192.168.1.102"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/bank-servers",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                },
                bank_server_create_params.BankServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServer,
        )

    def retrieve(
        self,
        server_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServer:
        """
        Retrieve a bank server.

        Get details of a bank server by its unique identifier.

        Args: server_id (int): ID of the bank server to retrieve.

        Returns: BankServerSchema: Details of the requested bank server.

        Example Request:

        ```
        GET / bank - servers / 1
        ```

        Example Response:

        ```json
        {
          "id": 1,
          "name": "Main Bank Server",
          "server_ip_address": "192.168.1.100"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/bank-servers/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServer,
        )

    def update(
        self,
        server_id: int,
        *,
        id: int,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServer:
        """
        Update a bank server.

        Modify the details of an existing bank server by its unique identifier.

        Args: server_id (int): ID of the bank server to update. payload
        (BankServerSchema): New details for the bank server.

        Returns: BankServerSchema: Updated details of the bank server.

        Example Request:

        ```json
        {
          "name": "Updated Bank Server",
          "server_ip_address": "192.168.1.103"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "name": "Updated Bank Server",
          "server_ip_address": "192.168.1.103"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/api/bank-servers/{server_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                },
                bank_server_update_params.BankServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServer,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServerListResponse:
        """
        List all bank servers.

        Retrieve a list of all bank servers registered in the system.

        Returns: List[BankServerSchema]: List of bank server details.

        Example Response:

        ```json
        [
          {
            "id": 1,
            "name": "Main Bank Server",
            "server_ip_address": "192.168.1.100"
          },
          {
            "id": 2,
            "name": "Backup Bank Server",
            "server_ip_address": "192.168.1.101"
          }
        ]
        ```
        """
        return self._get(
            "/api/bank-servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServerListResponse,
        )

    def delete(
        self,
        server_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bank server.

        Remove a bank server from the system by its unique identifier.

        Args: server_id (int): ID of the bank server to delete.

        Returns: 204: Successful deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/bank-servers/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBankServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBankServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBankServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBankServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#with_streaming_response
        """
        return AsyncBankServersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: int,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServer:
        """
        Create a new bank server.

        Add a new bank server to the system with the provided details.

        Args: payload (BankServerSchema): Details of the new bank server.

        Returns: BankServerSchema: Details of the created bank server.

        Example Request:

        ```json
        {
          "name": "New Bank Server",
          "server_ip_address": "192.168.1.102"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "name": "New Bank Server",
          "server_ip_address": "192.168.1.102"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/bank-servers",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                },
                bank_server_create_params.BankServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServer,
        )

    async def retrieve(
        self,
        server_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServer:
        """
        Retrieve a bank server.

        Get details of a bank server by its unique identifier.

        Args: server_id (int): ID of the bank server to retrieve.

        Returns: BankServerSchema: Details of the requested bank server.

        Example Request:

        ```
        GET / bank - servers / 1
        ```

        Example Response:

        ```json
        {
          "id": 1,
          "name": "Main Bank Server",
          "server_ip_address": "192.168.1.100"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/bank-servers/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServer,
        )

    async def update(
        self,
        server_id: int,
        *,
        id: int,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServer:
        """
        Update a bank server.

        Modify the details of an existing bank server by its unique identifier.

        Args: server_id (int): ID of the bank server to update. payload
        (BankServerSchema): New details for the bank server.

        Returns: BankServerSchema: Updated details of the bank server.

        Example Request:

        ```json
        {
          "name": "Updated Bank Server",
          "server_ip_address": "192.168.1.103"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "name": "Updated Bank Server",
          "server_ip_address": "192.168.1.103"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/api/bank-servers/{server_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                },
                bank_server_update_params.BankServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServer,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankServerListResponse:
        """
        List all bank servers.

        Retrieve a list of all bank servers registered in the system.

        Returns: List[BankServerSchema]: List of bank server details.

        Example Response:

        ```json
        [
          {
            "id": 1,
            "name": "Main Bank Server",
            "server_ip_address": "192.168.1.100"
          },
          {
            "id": 2,
            "name": "Backup Bank Server",
            "server_ip_address": "192.168.1.101"
          }
        ]
        ```
        """
        return await self._get(
            "/api/bank-servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankServerListResponse,
        )

    async def delete(
        self,
        server_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bank server.

        Remove a bank server from the system by its unique identifier.

        Args: server_id (int): ID of the bank server to delete.

        Returns: 204: Successful deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/bank-servers/{server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BankServersResourceWithRawResponse:
    def __init__(self, bank_servers: BankServersResource) -> None:
        self._bank_servers = bank_servers

        self.create = to_raw_response_wrapper(
            bank_servers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bank_servers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bank_servers.update,
        )
        self.list = to_raw_response_wrapper(
            bank_servers.list,
        )
        self.delete = to_raw_response_wrapper(
            bank_servers.delete,
        )


class AsyncBankServersResourceWithRawResponse:
    def __init__(self, bank_servers: AsyncBankServersResource) -> None:
        self._bank_servers = bank_servers

        self.create = async_to_raw_response_wrapper(
            bank_servers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bank_servers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bank_servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            bank_servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bank_servers.delete,
        )


class BankServersResourceWithStreamingResponse:
    def __init__(self, bank_servers: BankServersResource) -> None:
        self._bank_servers = bank_servers

        self.create = to_streamed_response_wrapper(
            bank_servers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bank_servers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bank_servers.update,
        )
        self.list = to_streamed_response_wrapper(
            bank_servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            bank_servers.delete,
        )


class AsyncBankServersResourceWithStreamingResponse:
    def __init__(self, bank_servers: AsyncBankServersResource) -> None:
        self._bank_servers = bank_servers

        self.create = async_to_streamed_response_wrapper(
            bank_servers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bank_servers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bank_servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bank_servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bank_servers.delete,
        )
