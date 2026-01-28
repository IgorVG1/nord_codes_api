import allure

from test.clients.transaction.transaction_schema import CreateTransactionResponseSchema, CreateTransactionQuerySchema, \
    ErrorCreateTransactionResponseSchema
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
    logger.info('Check create transaction response')

    assert_equal(actual=response.result,
                 expected='OK',
                 name='result')
    assert_equal(actual = response.balance,
                 expected = 10000 - query.amount,
                 name='balance')


@allure.step("Check create transaction response with bet bigger balance")
def assert_create_transaction_response_with_bet_bigger_balance(response: ErrorCreateTransactionResponseSchema):
    """
    Проверяет, что фактические данные ошибки о транзакции соответствуют ожидаемым.

    :param response: Фактические данные ошибки транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create transaction response with bet bigger balance')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual = response.message,
                 expected = 'Not enough money',
                 name='message')


@allure.step("Check create transaction response with empty amount")
def assert_create_transaction_response_with_empty_amount(response: ErrorCreateTransactionResponseSchema):
    """
    Проверяет, что фактические данные ошибки о транзакции соответствуют ожидаемым.

    :param response: Фактические данные ошибки транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create transaction response with empty amount')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual = response.message,
                 expected = 'amount: must not be null',
                 name='message')


@allure.step("Check create transaction response with invalid amount")
def assert_create_transaction_response_with_invalid_amount(query: CreateTransactionQuerySchema, response: ErrorCreateTransactionResponseSchema):
    """
    Проверяет, что фактические данные ошибки о транзакции соответствуют ожидаемым.

    :param query: Ожидаемые данные транзакции.
    :param response: Фактические данные ошибки транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create transaction response with invalid amount')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual = response.message,
                 expected = f"amount: Failed to convert value of type 'java.lang.String' to required type 'java.math.BigDecimal'; Character {query.amount} is neither a decimal digit number, decimal point, nor \"e\" notation exponential mark.",
                 name='message')


@allure.step("Check create transaction response by unauthorized user")
def assert_create_transaction_response_by_unauthorized_user(response: ErrorCreateTransactionResponseSchema):
    """
    Проверяет, что фактические данные ошибки о транзакции соответствуют ожидаемым.

    :param response: Фактические данные ошибки транзакции.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create transaction response by unauthorized user')

    assert_equal(actual=response.result,
                 expected='ERROR',
                 name='result')
    assert_equal(actual = response.message,
                 expected = 'Missing or invalid API Key',
                 name='message')