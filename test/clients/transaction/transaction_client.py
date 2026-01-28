import allure
from httpx import Response

from test.clients.api_client import APIClient
from test.clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from test.clients.public_http_builder import get_public_http_client
from test.clients.transaction.transaction_schema import CreateTransactionQuerySchema, CreateTransactionResponseSchema
from test.tools.routes import APIRoutes


class TransactionClient(APIClient):
    """
    Клиент для работы с /transaction
    """
    @allure.step('Create transaction')
    def create_transaction_api(self, query: CreateTransactionQuerySchema) -> Response:
        """
        Метод создания транзакции.

        :param query: Словарь с action и amount.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{APIRoutes.TRANSACTION}',
                         params=query.model_dump())


    @allure.step('Deserialization of response-body on "create transaction"')
    def create_transaction(self, query: CreateTransactionQuerySchema) -> CreateTransactionResponseSchema:
        """
        Десериализация ответа о создании транзакции.

        :param query: Словарь с action и amount.
        :return: Десериализованный ответ от сервера в виде модели CreateTransactionResponseSchema.
        """
        response = self.create_transaction_api(query=query)
        return CreateTransactionResponseSchema.model_validate_json(response.text)


def get_transaction_client(user: AuthenticationUserSchema) -> TransactionClient:
    """
    Функция создаёт экземпляр TransactionClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию TransactionClient.
    """
    return TransactionClient(client=get_private_http_client(user=user))


def get_unauthorized_transaction_client() -> TransactionClient:
    """
    Функция создаёт экземпляр TransactionClient с уже настроенным HTTP-клиентом без авторизации.

    :return: Готовый к использованию TransactionClient.
    """
    return TransactionClient(client=get_public_http_client())