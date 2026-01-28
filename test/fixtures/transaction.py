import pytest
from pydantic import BaseModel

from test.clients.transaction.transaction_client import TransactionClient, get_transaction_client, \
    get_unauthorized_transaction_client
from test.clients.transaction.transaction_schema import CreateTransactionQuerySchema, CreateTransactionResponseSchema
from test.fixtures.authentication import UserFixture


class TransactionFixture(BaseModel):
    """
    Модель данных, хранящая как запрос, так и ответ на создание транзакции.
    """
    query: CreateTransactionQuerySchema
    response: CreateTransactionResponseSchema



@pytest.fixture(scope='function')
def transaction_client(function_user: UserFixture) -> TransactionClient:
    """
    Фикстура, которая возвращает настроенный клиент для работы с /transaction.

    :param function_user: Фикстура с учетными данными пользователя.
    :return: TransactionClient: Экземпляр TransactionClient с уже настроенным HTTP-клиентом.
    """
    return get_transaction_client(user=function_user.authentication_user)


@pytest.fixture(scope='function')
def unauthorized_transaction_client() -> TransactionClient:
    """
    Фикстура, которая возвращает настроенный клиент для работы с /transaction.

    :return: TransactionClient: Экземпляр TransactionClient с уже настроенным HTTP-клиентом.
    """
    return get_unauthorized_transaction_client()


@pytest.fixture(scope='function')
def function_transaction(transaction_client: TransactionClient) -> TransactionFixture:
    """

    Фикстура, которая возвращает уже созданную транзакцию.

    :param transaction_client: Фикстура с уже настроенным HTTP-клиентом типа TransactionClient
    :return: TransactionFixture: Модель данных созданной транзакции.
    """
    query = CreateTransactionQuerySchema()
    response = transaction_client.create_transaction(query=query)
    return TransactionFixture(query=query,
                              response=response)