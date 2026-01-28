import allure
from httpx import Response
from test.clients.api_client import APIClient
from test.clients.authentication.authentication_schema import AuthorizationQuerySchema, AuthorizationResponseSchema
from test.clients.public_http_builder import get_public_http_client
from test.tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/token/
    """
    @allure.step('Get access token used by username and password')
    def authorization_api(self, query: AuthorizationQuerySchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param query: Словарь с username и password.
        :return: Ответ от сервера.
        """
        return self.post(url=f'{APIRoutes.AUTHENTICATION}',
                         params=query.model_dump())

    def authorization(self, query: AuthorizationQuerySchema) -> AuthorizationResponseSchema:
        """
        Метод выполняет десериализацию ответа сервера на аутентификацию пользователя.

        :param query: Словарь с username и password.
        :return: LoginResponseSchema: pydantic-model ответа от сервера
        """
        response = self.authorization_api(query=query)
        return AuthorizationResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())