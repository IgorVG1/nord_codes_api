import pytest, allure

from http import HTTPStatus

from test.clients.authentication.authentication_client import AuthenticationClient
from test.clients.transaction.transaction_client import TransactionClient
from test.clients.transaction.transaction_schema import CreateTransactionQuerySchema, CreateTransactionResponseSchema, \
    ErrorCreateTransactionResponseSchema
from test.test_suits.transaction.data import AMOUNT_400
from test.test_suits.transaction.transaction_assertions import assert_create_transaction_response, \
    assert_create_transaction_response_with_bet_bigger_balance, assert_create_transaction_response_with_invalid_amount, \
    assert_create_transaction_response_by_unauthorized_user
from test.tools.allure.epics import AllureEpic
from test.tools.allure.features import AllureFeature
from test.tools.allure.severity import AllureSeverity
from test.tools.allure.stories import AllureStory
from test.tools.allure.tags import AllureTag
from test.tools.assertions.base import assert_status_code
from test.tools.assertions.schema import validate_json_schema


@pytest.mark.transaction
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.TRANSACTION)
@allure.epic(AllureEpic.NORD_CODES)
@allure.feature(AllureFeature.TRANSACTION)
@allure.parent_suite(AllureEpic.NORD_CODES)
@allure.suite(AllureFeature.TRANSACTION)
class TestTransaction:

    @pytest.mark.flaky(reruns=3, reruns_delay=5)
    @allure.title("[200]OK - Create transaction")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.CRITICAL)
    def test_create_transaction(self, transaction_client: TransactionClient):
        query = CreateTransactionQuerySchema()
        response = transaction_client.create_transaction_api(query=query)
        response_data = CreateTransactionResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.OK)
        assert_create_transaction_response(query=query,
                                           response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.flaky(reruns=3, reruns_delay=5)
    @allure.title("[402]PAYMENT_REQUIRED - Create transaction with bet bigger balance")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_create_transaction_with_bet_bigger_balance(self, transaction_client: TransactionClient):
        query = CreateTransactionQuerySchema(amount=11000)
        response = transaction_client.create_transaction_api(query=query)
        response_data = ErrorCreateTransactionResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.PAYMENT_REQUIRED)
        assert_create_transaction_response_with_bet_bigger_balance(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.parametrize('amount_400', AMOUNT_400)
    @allure.title("[400]BAD_REQUEST - Create transaction with invalid amount")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_create_transaction_with_invalid_amount(self, amount_400: str, transaction_client: TransactionClient):
        query = CreateTransactionQuerySchema(amount=amount_400)
        response = transaction_client.create_transaction_api(query=query)
        response_data = ErrorCreateTransactionResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.BAD_REQUEST)
        assert_create_transaction_response_with_invalid_amount(query=query,
                                                               response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.parametrize('amount_400', AMOUNT_400)
    @allure.title("[400]BAD_REQUEST - Create transaction with invalid amount")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_create_transaction_with_invalid_amount(self, amount_400: str, transaction_client: TransactionClient):
        query = CreateTransactionQuerySchema(amount=amount_400)
        response = transaction_client.create_transaction_api(query=query)
        response_data = ErrorCreateTransactionResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.BAD_REQUEST)
        assert_create_transaction_response_with_invalid_amount(query=query,
                                                               response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    @allure.title("[401]UNAUTHORIZED - Create transaction by unauthorized user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_create_transaction_with_invalid_amount(self, unauthorized_transaction_client: TransactionClient):
        query = CreateTransactionQuerySchema()
        response = unauthorized_transaction_client.create_transaction_api(query=query)
        response_data = ErrorCreateTransactionResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.UNAUTHORIZED)
        assert_create_transaction_response_by_unauthorized_user(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())