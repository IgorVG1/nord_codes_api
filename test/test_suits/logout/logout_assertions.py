import allure

from test.clients.logout.logout_schema import LogoutResponseSchema, ErrorLogoutResponseSchema
from test.clients.transaction.transaction_schema import ErrorCreateTransactionResponseSchema
from test.tools.assertions.base import assert_equal
from test.tools.logger import get_logger


logger = get_logger("LOGOUT_ASSERTIONS")


@allure.step("Check log out response")
def assert_logout_response(response: LogoutResponseSchema):
    """
    Проверяет, что фактические данные ответа о выходе из системы соответствуют ожидаемым.

    :param response: Фактические данные транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check log out response')

    assert_equal(actual=response.result,
                 expected='OK',
                 name='result')


@allure.step("Check log out response with verify token status")
def assert_logout_response_with_verify_token_status(response_transaction_error: ErrorCreateTransactionResponseSchema):
    """
    Проверяет, что после успешного завершения сессии невозможно создать транзакцию, так как token удален.

    :param response_transaction_error: Фактические данные транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check log out response with verify token status')

    assert_equal(actual=response_transaction_error.result,
                 expected='ERROR',
                 name='result')

    assert_equal(actual=response_transaction_error.message,
                 expected='Missing or invalid API Key',
                 name='message')


@allure.step("Check log out response by unauthorized user")
def assert_logout_response_by_unauthorized_user(response: ErrorLogoutResponseSchema):
    """
    Проверяет, что невозможно выполнить завершение сессии неавторизованным пользователем.

    :param response: Фактические данные транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check log out response by unauthorized user')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')

    assert_equal(actual=response.message,
                 expected='Missing or invalid API Key',
                 name='message')