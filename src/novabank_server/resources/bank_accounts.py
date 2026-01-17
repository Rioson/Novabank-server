# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bank_account_create_params, bank_account_update_params
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
from ..types.bank_account import BankAccount
from ..types.bank_account_list_response import BankAccountListResponse

__all__ = ["BankAccountsResource", "AsyncBankAccountsResource"]


class BankAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BankAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Rioson/Novabank-server#accessing-raw-response-data-eg-headers
        """
        return BankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BankAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Rioson/Novabank-server#with_streaming_response
        """
        return BankAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_name: str,
        account_number: str,
        bank_server: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """
        Create a new bank account.

        Add a new bank account to the system with the provided details.

        Args: payload (BankAccountCreateSchema): Details of the new bank account.

        Returns: BankAccountSchema: Details of the created bank account.

        Example Request:

        ```json
        {
          "bank_server": 1,
          "account_name": "Payroll Account",
          "account_number": "987654321"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "bank_server": {
            "id": 1,
            "name": "Main Bank Server",
            "server_ip_address": "192.168.1.100"
          },
          "account_name": "Payroll Account",
          "account_number": "987654321"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/bank-accounts",
            body=maybe_transform(
                {
                    "account_name": account_name,
                    "account_number": account_number,
                    "bank_server": bank_server,
                },
                bank_account_create_params.BankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
        )

    def retrieve(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """
        Get a bank account.

        Retrieve the details of a bank account by its unique identifier.

        Args: account_id (int): ID of the bank account to retrieve.

        Returns: BankAccountSchema: Details of the requested bank account.

        Example Request:

        ```
        GET / bank - accounts / 1
        ```

        Example Response:

        ```json
        {
          "id": 1,
          "bank_server": {
            "id": 1,
            "name": "Main Bank Server",
            "server_ip_address": "192.168.1.100"
          },
          "account_name": "Checking Account",
          "account_number": "123456789"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/bank-accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
        )

    def update(
        self,
        account_id: int,
        *,
        account_name: str,
        account_number: str,
        bank_server: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """
        Update a bank account.

        Modify the details of a bank account by its unique identifier.

        Args: account_id (int): ID of the bank account to update. payload
        (BankAccountCreateSchema): New details for the bank account.

        Returns: BankAccountSchema: Updated details of the bank account.

        Example Request:

        ```json
        {
          "bank_server": 2,
          "account_name": "Updated Savings Account",
          "account_number": "654321987"
        }
        ```

        Example Response:

        ```json
        {
          "id": 2,
          "bank_server": {
            "id": 2,
            "name": "Backup Bank Server",
            "server_ip_address": "192.168.1.101"
          },
          "account_name": "Updated Savings Account",
          "account_number": "654321987"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/api/bank-accounts/{account_id}",
            body=maybe_transform(
                {
                    "account_name": account_name,
                    "account_number": account_number,
                    "bank_server": bank_server,
                },
                bank_account_update_params.BankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
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
    ) -> BankAccountListResponse:
        """
        Get a list of all bank accounts.

        Retrieve a list of all bank accounts registered in the system.

        Returns: List[BankAccountSchema]: List of bank account details.

        Example Response:

        ```json
        [
          {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          {
            "id": 2,
            "bank_server": {
              "id": 2,
              "name": "Backup Bank Server",
              "server_ip_address": "192.168.1.101"
            },
            "account_name": "Savings Account",
            "account_number": "987654321"
          }
        ]
        ```
        """
        return self._get(
            "/api/bank-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccountListResponse,
        )

    def delete(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bank account.

        Remove a bank account from the system by its unique identifier.

        Args: account_id (int): ID of the bank account to delete.

        Returns: 204: Successful deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/bank-accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBankAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBankAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Rioson/Novabank-server#accessing-raw-response-data-eg-headers
        """
        return AsyncBankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Rioson/Novabank-server#with_streaming_response
        """
        return AsyncBankAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_name: str,
        account_number: str,
        bank_server: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """
        Create a new bank account.

        Add a new bank account to the system with the provided details.

        Args: payload (BankAccountCreateSchema): Details of the new bank account.

        Returns: BankAccountSchema: Details of the created bank account.

        Example Request:

        ```json
        {
          "bank_server": 1,
          "account_name": "Payroll Account",
          "account_number": "987654321"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "bank_server": {
            "id": 1,
            "name": "Main Bank Server",
            "server_ip_address": "192.168.1.100"
          },
          "account_name": "Payroll Account",
          "account_number": "987654321"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/bank-accounts",
            body=await async_maybe_transform(
                {
                    "account_name": account_name,
                    "account_number": account_number,
                    "bank_server": bank_server,
                },
                bank_account_create_params.BankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
        )

    async def retrieve(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """
        Get a bank account.

        Retrieve the details of a bank account by its unique identifier.

        Args: account_id (int): ID of the bank account to retrieve.

        Returns: BankAccountSchema: Details of the requested bank account.

        Example Request:

        ```
        GET / bank - accounts / 1
        ```

        Example Response:

        ```json
        {
          "id": 1,
          "bank_server": {
            "id": 1,
            "name": "Main Bank Server",
            "server_ip_address": "192.168.1.100"
          },
          "account_name": "Checking Account",
          "account_number": "123456789"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/bank-accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
        )

    async def update(
        self,
        account_id: int,
        *,
        account_name: str,
        account_number: str,
        bank_server: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """
        Update a bank account.

        Modify the details of a bank account by its unique identifier.

        Args: account_id (int): ID of the bank account to update. payload
        (BankAccountCreateSchema): New details for the bank account.

        Returns: BankAccountSchema: Updated details of the bank account.

        Example Request:

        ```json
        {
          "bank_server": 2,
          "account_name": "Updated Savings Account",
          "account_number": "654321987"
        }
        ```

        Example Response:

        ```json
        {
          "id": 2,
          "bank_server": {
            "id": 2,
            "name": "Backup Bank Server",
            "server_ip_address": "192.168.1.101"
          },
          "account_name": "Updated Savings Account",
          "account_number": "654321987"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/api/bank-accounts/{account_id}",
            body=await async_maybe_transform(
                {
                    "account_name": account_name,
                    "account_number": account_number,
                    "bank_server": bank_server,
                },
                bank_account_update_params.BankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
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
    ) -> BankAccountListResponse:
        """
        Get a list of all bank accounts.

        Retrieve a list of all bank accounts registered in the system.

        Returns: List[BankAccountSchema]: List of bank account details.

        Example Response:

        ```json
        [
          {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          {
            "id": 2,
            "bank_server": {
              "id": 2,
              "name": "Backup Bank Server",
              "server_ip_address": "192.168.1.101"
            },
            "account_name": "Savings Account",
            "account_number": "987654321"
          }
        ]
        ```
        """
        return await self._get(
            "/api/bank-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccountListResponse,
        )

    async def delete(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bank account.

        Remove a bank account from the system by its unique identifier.

        Args: account_id (int): ID of the bank account to delete.

        Returns: 204: Successful deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/bank-accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = to_raw_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bank_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bank_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            bank_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            bank_accounts.delete,
        )


class AsyncBankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = async_to_raw_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bank_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bank_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            bank_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bank_accounts.delete,
        )


class BankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = to_streamed_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bank_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bank_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            bank_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            bank_accounts.delete,
        )


class AsyncBankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = async_to_streamed_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bank_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bank_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bank_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bank_accounts.delete,
        )
