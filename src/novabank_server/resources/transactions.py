# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import transaction_create_params, transaction_update_status_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.transaction import Transaction
from ..types.transaction_list_response import TransactionListResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: float,
        source_account: int,
        transaction_type: str,
        provider: Optional[str] | Omit = omit,
        target_bank_account_number: Optional[str] | Omit = omit,
        target_bank_name: Optional[str] | Omit = omit,
        target_country: Optional[str] | Omit = omit,
        target_iban: Optional[str] | Omit = omit,
        target_phone_number: Optional[str] | Omit = omit,
        target_swift_code: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a new transaction.

        Add a new transaction to the system, either a bank transfer or mobile money
        transfer. This API endpoint is used to transfer money from the bank server to
        the selected bank account globally.

        Args: payload (TransactionCreateSchema): Details of the new transaction.

        Returns: TransactionSchema: Details of the created transaction.

        Example Request (Bank Transfer):

        ```json
        {
          "transaction_type": "bank_transfer",
          "amount": 500.0,
          "source_account": 1,
          "target_iban": "GB0011223344",
          "target_swift_code": "BANKGB22",
          "target_bank_account_number": "55667788",
          "target_bank_name": "UK Bank",
          "target_country": "United Kingdom",
          "provider": "SWIFT"
        }
        ```

        Example Response (Bank Transfer):

        ```json
        {
          "id": 3,
          "transaction_type": "bank_transfer",
          "amount": 500.0,
          "source_account": {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          "target_iban": "GB0011223344",
          "target_swift_code": "BANKGB22",
          "target_bank_account_number": "55667788",
          "target_bank_name": "UK Bank",
          "target_country": "United Kingdom",
          "provider": "SWIFT",
          "status": "pending"
        }
        ```

        Example Request (Mobile Transfer):

        ```json
        {
          "transaction_type": "mobile_transfer",
          "amount": 50.0,
          "source_account": 2,
          "target_phone_number": "+1 555-1234",
          "provider": "CashApp"
        }
        ```

        Example Response (Mobile Transfer):

        ```json
        {
          "id": 4,
          "transaction_type": "mobile_transfer",
          "amount": 50.0,
          "source_account": {
            "id": 2,
            "bank_server": {
              "id": 2,
              "name": "Backup Bank Server",
              "server_ip_address": "192.168.1.101"
            },
            "account_name": "Savings Account",
            "account_number": "987654321"
          },
          "target_phone_number": "+1 555-1234",
          "provider": "CashApp",
          "status": "pending"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/transactions",
            body=maybe_transform(
                {
                    "amount": amount,
                    "source_account": source_account,
                    "transaction_type": transaction_type,
                    "provider": provider,
                    "target_bank_account_number": target_bank_account_number,
                    "target_bank_name": target_bank_name,
                    "target_country": target_country,
                    "target_iban": target_iban,
                    "target_phone_number": target_phone_number,
                    "target_swift_code": target_swift_code,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        transaction_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transaction:
        """
        Retrieve a transaction.

        Get details of a transaction by its unique identifier.

        Args: transaction_id (int): ID of the transaction to retrieve.

        Returns: TransactionSchema: Details of the requested transaction.

        Example Request:

        ```
        GET / transactions / 1
        ```

        Example Response:

        ```json
        {
          "id": 1,
          "transaction_type": "bank_transfer",
          "amount": 1000.0,
          "source_account": {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          "target_iban": "DE1234567890",
          "target_swift_code": "BANKDEFF",
          "target_bank_account_number": "987654321",
          "target_bank_name": "Foreign Bank",
          "target_country": "Germany",
          "provider": "TransferWise",
          "status": "pending"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/transactions/{transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transaction,
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
    ) -> TransactionListResponse:
        """
        List all transactions.

        Retrieve a list of all transactions that have occurred.

        Returns: List[TransactionSchema]: List of transaction details.

        Example Response:

        ```json
        [
          {
            "id": 1,
            "transaction_type": "bank_transfer",
            "amount": 1000.0,
            "source_account": {
              "id": 1,
              "bank_server": {
                "id": 1,
                "name": "Main Bank Server",
                "server_ip_address": "192.168.1.100"
              },
              "account_name": "Checking Account",
              "account_number": "123456789"
            },
            "target_iban": "DE1234567890",
            "target_swift_code": "BANKDEFF",
            "target_bank_account_number": "987654321",
            "target_bank_name": "Foreign Bank",
            "target_country": "Germany",
            "provider": "TransferWise",
            "status": "pending"
          },
          {
            "id": 2,
            "transaction_type": "mobile_transfer",
            "amount": 50.0,
            "source_account": {
              "id": 2,
              "bank_server": {
                "id": 2,
                "name": "Backup Bank Server",
                "server_ip_address": "192.168.1.101"
              },
              "account_name": "Savings Account",
              "account_number": "987654321"
            },
            "target_phone_number": "+1 555-1234",
            "provider": "CashApp",
            "status": "completed"
          }
        ]
        ```
        """
        return self._get(
            "/api/transactions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionListResponse,
        )

    def delete(
        self,
        transaction_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a transaction.

        Remove a transaction from the system by its unique identifier.

        Args: transaction_id (int): ID of the transaction to delete.

        Returns: 204: Successful deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/transactions/{transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_status(
        self,
        transaction_id: int,
        *,
        status: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transaction:
        """
        Update the status of a transaction.

        Modify the status of an existing transaction by its unique identifier.

        Args: transaction_id (int): ID of the transaction to update. payload
        (TransactionStatusUpdateSchema): New status for the transaction.

        Returns: TransactionSchema: Updated details of the transaction.

        Example Request:

        ```json
        {
          "status": "completed"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "transaction_type": "bank_transfer",
          "amount": 500.0,
          "source_account": {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          "target_iban": "GB0011223344",
          "target_swift_code": "BANKGB22",
          "target_bank_account_number": "55667788",
          "target_bank_name": "UK Bank",
          "target_country": "United Kingdom",
          "provider": "SWIFT",
          "status": "completed"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/api/transactions/{transaction_id}/status",
            body=maybe_transform({"status": status}, transaction_update_status_params.TransactionUpdateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transaction,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/novabank-server-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: float,
        source_account: int,
        transaction_type: str,
        provider: Optional[str] | Omit = omit,
        target_bank_account_number: Optional[str] | Omit = omit,
        target_bank_name: Optional[str] | Omit = omit,
        target_country: Optional[str] | Omit = omit,
        target_iban: Optional[str] | Omit = omit,
        target_phone_number: Optional[str] | Omit = omit,
        target_swift_code: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a new transaction.

        Add a new transaction to the system, either a bank transfer or mobile money
        transfer. This API endpoint is used to transfer money from the bank server to
        the selected bank account globally.

        Args: payload (TransactionCreateSchema): Details of the new transaction.

        Returns: TransactionSchema: Details of the created transaction.

        Example Request (Bank Transfer):

        ```json
        {
          "transaction_type": "bank_transfer",
          "amount": 500.0,
          "source_account": 1,
          "target_iban": "GB0011223344",
          "target_swift_code": "BANKGB22",
          "target_bank_account_number": "55667788",
          "target_bank_name": "UK Bank",
          "target_country": "United Kingdom",
          "provider": "SWIFT"
        }
        ```

        Example Response (Bank Transfer):

        ```json
        {
          "id": 3,
          "transaction_type": "bank_transfer",
          "amount": 500.0,
          "source_account": {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          "target_iban": "GB0011223344",
          "target_swift_code": "BANKGB22",
          "target_bank_account_number": "55667788",
          "target_bank_name": "UK Bank",
          "target_country": "United Kingdom",
          "provider": "SWIFT",
          "status": "pending"
        }
        ```

        Example Request (Mobile Transfer):

        ```json
        {
          "transaction_type": "mobile_transfer",
          "amount": 50.0,
          "source_account": 2,
          "target_phone_number": "+1 555-1234",
          "provider": "CashApp"
        }
        ```

        Example Response (Mobile Transfer):

        ```json
        {
          "id": 4,
          "transaction_type": "mobile_transfer",
          "amount": 50.0,
          "source_account": {
            "id": 2,
            "bank_server": {
              "id": 2,
              "name": "Backup Bank Server",
              "server_ip_address": "192.168.1.101"
            },
            "account_name": "Savings Account",
            "account_number": "987654321"
          },
          "target_phone_number": "+1 555-1234",
          "provider": "CashApp",
          "status": "pending"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/transactions",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "source_account": source_account,
                    "transaction_type": transaction_type,
                    "provider": provider,
                    "target_bank_account_number": target_bank_account_number,
                    "target_bank_name": target_bank_name,
                    "target_country": target_country,
                    "target_iban": target_iban,
                    "target_phone_number": target_phone_number,
                    "target_swift_code": target_swift_code,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        transaction_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transaction:
        """
        Retrieve a transaction.

        Get details of a transaction by its unique identifier.

        Args: transaction_id (int): ID of the transaction to retrieve.

        Returns: TransactionSchema: Details of the requested transaction.

        Example Request:

        ```
        GET / transactions / 1
        ```

        Example Response:

        ```json
        {
          "id": 1,
          "transaction_type": "bank_transfer",
          "amount": 1000.0,
          "source_account": {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          "target_iban": "DE1234567890",
          "target_swift_code": "BANKDEFF",
          "target_bank_account_number": "987654321",
          "target_bank_name": "Foreign Bank",
          "target_country": "Germany",
          "provider": "TransferWise",
          "status": "pending"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/transactions/{transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transaction,
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
    ) -> TransactionListResponse:
        """
        List all transactions.

        Retrieve a list of all transactions that have occurred.

        Returns: List[TransactionSchema]: List of transaction details.

        Example Response:

        ```json
        [
          {
            "id": 1,
            "transaction_type": "bank_transfer",
            "amount": 1000.0,
            "source_account": {
              "id": 1,
              "bank_server": {
                "id": 1,
                "name": "Main Bank Server",
                "server_ip_address": "192.168.1.100"
              },
              "account_name": "Checking Account",
              "account_number": "123456789"
            },
            "target_iban": "DE1234567890",
            "target_swift_code": "BANKDEFF",
            "target_bank_account_number": "987654321",
            "target_bank_name": "Foreign Bank",
            "target_country": "Germany",
            "provider": "TransferWise",
            "status": "pending"
          },
          {
            "id": 2,
            "transaction_type": "mobile_transfer",
            "amount": 50.0,
            "source_account": {
              "id": 2,
              "bank_server": {
                "id": 2,
                "name": "Backup Bank Server",
                "server_ip_address": "192.168.1.101"
              },
              "account_name": "Savings Account",
              "account_number": "987654321"
            },
            "target_phone_number": "+1 555-1234",
            "provider": "CashApp",
            "status": "completed"
          }
        ]
        ```
        """
        return await self._get(
            "/api/transactions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionListResponse,
        )

    async def delete(
        self,
        transaction_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a transaction.

        Remove a transaction from the system by its unique identifier.

        Args: transaction_id (int): ID of the transaction to delete.

        Returns: 204: Successful deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/transactions/{transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_status(
        self,
        transaction_id: int,
        *,
        status: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transaction:
        """
        Update the status of a transaction.

        Modify the status of an existing transaction by its unique identifier.

        Args: transaction_id (int): ID of the transaction to update. payload
        (TransactionStatusUpdateSchema): New status for the transaction.

        Returns: TransactionSchema: Updated details of the transaction.

        Example Request:

        ```json
        {
          "status": "completed"
        }
        ```

        Example Response:

        ```json
        {
          "id": 3,
          "transaction_type": "bank_transfer",
          "amount": 500.0,
          "source_account": {
            "id": 1,
            "bank_server": {
              "id": 1,
              "name": "Main Bank Server",
              "server_ip_address": "192.168.1.100"
            },
            "account_name": "Checking Account",
            "account_number": "123456789"
          },
          "target_iban": "GB0011223344",
          "target_swift_code": "BANKGB22",
          "target_bank_account_number": "55667788",
          "target_bank_name": "UK Bank",
          "target_country": "United Kingdom",
          "provider": "SWIFT",
          "status": "completed"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/api/transactions/{transaction_id}/status",
            body=await async_maybe_transform(
                {"status": status}, transaction_update_status_params.TransactionUpdateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transaction,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.create = to_raw_response_wrapper(
            transactions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transactions.list,
        )
        self.delete = to_raw_response_wrapper(
            transactions.delete,
        )
        self.update_status = to_raw_response_wrapper(
            transactions.update_status,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.create = async_to_raw_response_wrapper(
            transactions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            transactions.delete,
        )
        self.update_status = async_to_raw_response_wrapper(
            transactions.update_status,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.create = to_streamed_response_wrapper(
            transactions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )
        self.delete = to_streamed_response_wrapper(
            transactions.delete,
        )
        self.update_status = to_streamed_response_wrapper(
            transactions.update_status,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.create = async_to_streamed_response_wrapper(
            transactions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            transactions.delete,
        )
        self.update_status = async_to_streamed_response_wrapper(
            transactions.update_status,
        )
