from http import HTTPStatus

import pytest, allure

from test.clients.transaction.transaction_client import TransactionClient
from test.clients.transaction.transaction_schema import CreateTransactionQuerySchema, CreateTransactionResponseSchema
from test.test_suits.transaction.transaction_assertions import assert_create_transaction_response
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