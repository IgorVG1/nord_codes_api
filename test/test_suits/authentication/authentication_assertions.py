import allure

from test.clients.authentication.authentication_schema import InvalidAuthorizationResponseSchema
from test.tools.assertions.base import assert_equal
from test.tools.logger import get_logger


logger = get_logger("AUTHORIZATION_ASSERTIONS")


@allure.step("Check invalid authorization response with incorrect username or password")
def assert_invalid_authorization_response_with_incorrect_data(response: InvalidAuthorizationResponseSchema):
    """
    Проверяет, что фактические данные ответа о некорректной попытке входа в систему соответствуют ожидаемым.

    :param response: Фактические данные ответа об ошибке.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check invalid authorization response with incorrect username or password')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual=response.message,
                 expected='Invalid credentials',
                 name='message')


@allure.step("Check invalid authorization response with empty username")
def assert_invalid_authorization_response_with_empty_username(response: InvalidAuthorizationResponseSchema):
    """
    Проверяет, что фактические данные ответа о некорректной попытке входа в систему соответствуют ожидаемым.

    :param response: Фактические данные ответа об ошибке.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check invalid authorization response with empty username')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual=response.message,
                 expected='username: must not be blank',
                 name='message')


@allure.step("Check invalid authorization response with empty password")
def assert_invalid_authorization_response_with_empty_password(response: InvalidAuthorizationResponseSchema):
    """
    Проверяет, что фактические данные ответа о некорректной попытке входа в систему соответствуют ожидаемым.

    :param response: Фактические данные ответа об ошибке.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check invalid authorization response with empty password')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual=response.message,
                 expected='password: must not be blank',
                 name='message')


@allure.step("Check invalid authorization response with empty data")
def assert_invalid_authorization_response_with_empty_data(response: InvalidAuthorizationResponseSchema):
    """
    Проверяет, что фактические данные ответа о некорректной попытке входа в систему соответствуют ожидаемым.

    :param response: Фактические данные ответа об ошибке.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check invalid authorization response with empty data')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual=response.message,
                 expected='username: must not be blank; password: must not be blank',
                 name='message')