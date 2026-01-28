import pytest

from test.clients.logout.logout_client import LogoutClient, get_logout_client
from test.fixtures.authentication import UserFixture


@pytest.fixture(scope='function')
def logout_client(function_user: UserFixture) -> LogoutClient:
    """
    Фикстура, которая возвращает настроенный клиент для работы с /logout.

    :param function_user: Фикстура с учетными данными пользователя.
    :return: LogoutClient: Экземпляр LogoutClient с уже настроенным HTTP-клиентом.
    """
    return get_logout_client(user=function_user.authentication_user)