import pytest
from pydantic import BaseModel

from test.clients.logout.logout_client import LogoutClient, get_logout_client, get_unauthorized_logout_client
from test.clients.logout.logout_schema import LogoutResponseSchema
from test.fixtures.authentication import UserFixture


class LogoutFixture(BaseModel):
    response: LogoutResponseSchema


@pytest.fixture(scope='function')
def logout_client(function_user: UserFixture) -> LogoutClient:
    """
    Фикстура, которая возвращает настроенный клиент для работы с /logout.

    :param function_user: Фикстура с учетными данными пользователя.
    :return: LogoutClient: Экземпляр LogoutClient с уже настроенным HTTP-клиентом.
    """
    return get_logout_client(user=function_user.authentication_user)


@pytest.fixture(scope='function')
def unauthorized_logout_client() -> LogoutClient:
    """
    Фикстура, которая возвращает настроенный клиент для работы с /logout.

    :return: LogoutClient: Экземпляр LogoutClient с уже настроенным HTTP-клиентом.
    """
    return get_unauthorized_logout_client()

@pytest.fixture(scope='function')
def function_logout_client(logout_client: LogoutClient) -> LogoutFixture:
    """
    Фикстура производит завершение сессии.

    :param logout_client: Фикстура с уже настроенным HTTP-клиентом LogoutClient.
    :return: LogoutFixture - Модель с ответом об успешном выходе из системы.
    """
    response = logout_client.logout()
    return LogoutFixture(response=response)