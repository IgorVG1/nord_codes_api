import pytest, allure

from http import HTTPStatus
from test.clients.logout.logout_client import LogoutClient
from test.clients.logout.logout_schema import LogoutResponseSchema, ErrorLogoutResponseSchema
from test.clients.transaction.transaction_client import TransactionClient
from test.clients.transaction.transaction_schema import CreateTransactionResponseSchema, CreateTransactionQuerySchema, \
    ErrorCreateTransactionResponseSchema
from test.fixtures.logout import LogoutFixture
from test.test_suits.logout.logout_assertions import assert_logout_response, \
    assert_logout_response_with_verify_token_status, assert_logout_response_by_unauthorized_user
from test.tools.allure.epics import AllureEpic
from test.tools.allure.features import AllureFeature
from test.tools.allure.severity import AllureSeverity
from test.tools.allure.stories import AllureStory
from test.tools.allure.tags import AllureTag
from test.tools.assertions.base import assert_status_code
from test.tools.assertions.schema import validate_json_schema


@pytest.mark.logout
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.LOGOUT)
@allure.epic(AllureEpic.NORD_CODES)
@allure.feature(AllureFeature.LOGOUT)
@allure.parent_suite(AllureEpic.NORD_CODES)
@allure.suite(AllureFeature.LOGOUT)
class TestLogout:

    @allure.title("[200]OK - Successfully logged out")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_logout(self, logout_client: LogoutClient):
        response = logout_client.logout_api()
        response_data = LogoutResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.OK)
        assert_logout_response(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @allure.title("[401]UNAUTHORIZED - Successfully logged out with verify token status")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_logout_with_verify_token_status(self,
                                             function_logout_client: LogoutFixture,
                                             unauthorized_transaction_client: TransactionClient):
        query = CreateTransactionQuerySchema()
        response = unauthorized_transaction_client.create_transaction_api(query=query)
        response_data = ErrorCreateTransactionResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.UNAUTHORIZED)
        assert_logout_response_with_verify_token_status(response_transaction_error=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @allure.title("[401]UNAUTHORIZED - Logged out by unauthorized user")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_logout_by_unauthorized_user(self, unauthorized_logout_client: LogoutClient):
        response = unauthorized_logout_client.logout_api()
        response_data = ErrorLogoutResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code,
                           expected=HTTPStatus.UNAUTHORIZED)
        assert_logout_response_by_unauthorized_user(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())