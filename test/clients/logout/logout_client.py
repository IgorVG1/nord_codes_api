import allure
from httpx import Response

from test.clients.api_client import APIClient
from test.clients.logout.logout_schema import LogoutResponseSchema
from test.clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from test.tools.routes import APIRoutes


class LogoutClient(APIClient):
    """
    Клиент для работы с /logout
    """
    @allure.step('Log out from session')
    def logout_api(self) -> Response:
        """
        Метод создания транзакции.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{APIRoutes.LOGOUT}')


    @allure.step('Deserialization of response-body on "log out from session"')
    def logout(self) -> LogoutResponseSchema:
        """
        Десериализация ответа о завершении сессии.

        :return: Десериализованный ответ от сервера в виде модели LogoutResponseSchema.
        """
        response = self.logout_api()
        return LogoutResponseSchema.model_validate_json(response.text)


def get_logout_client(user: AuthenticationUserSchema) -> LogoutClient:
    """
    Функция создаёт экземпляр LogoutClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию LogoutClient.
    """
    return LogoutClient(client=get_private_http_client(user=user))