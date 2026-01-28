import allure

from test.clients.logout.logout_schema import LogoutResponseSchema
from test.clients.transaction.transaction_schema import CreateTransactionResponseSchema, CreateTransactionQuerySchema
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