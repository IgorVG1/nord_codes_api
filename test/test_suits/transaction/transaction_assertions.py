import allure

from test.clients.transaction.transaction_schema import CreateTransactionResponseSchema, CreateTransactionQuerySchema
from test.tools.assertions.base import assert_equal
from test.tools.logger import get_logger


logger = get_logger("TRANSACTION_ASSERTIONS")


@allure.step("Check create transaction response")
def assert_create_transaction_response(query: CreateTransactionQuerySchema, response: CreateTransactionResponseSchema):
    """
    Проверяет, что фактические данные транзакции соответствуют ожидаемым.

    :param response: Фактические данные транзакции.
    :param query: Ожидаемые данные транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create exercise response')

    assert_equal(actual=response.result,
                 expected='OK',
                 name='result')
    assert_equal(actual = response.balance,
                 expected = 10000 - query.amount,
                 name='balance')