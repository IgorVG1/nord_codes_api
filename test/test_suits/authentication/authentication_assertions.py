import allure

from test.clients.authentication.authentication_schema import InvalidLoginResponseSchema
from test.tools.assertions.base import assert_equal
from test.tools.logger import get_logger


logger = get_logger('AUTHENTICATION_ASSERTIONS')


@allure.step('Check success authorization response')
def assert_success_authorization_response(response: InvalidLoginResponseSchema):
    """
    Проверяет структуру предупреждения о некорректном создании дополнительного фильтра.
    [412]PRECONDITION_FAILED - Не указано направление правила дополнительной фильтрации

    :param response: Ответ API строкового типа.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected = "user not found"
    assert_equal(actual=response.detail,
                 expected=expected,
                 name='detail')