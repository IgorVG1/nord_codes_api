import allure, pytest
from http import HTTPStatus

from test.clients.authentication.authentication_client import AuthenticationClient
from test.clients.authentication.authentication_schema import AuthorizationQuerySchema, AuthorizationResponseSchema
from test.tools.allure.epics import AllureEpic
from test.tools.allure.features import AllureFeature
from test.tools.allure.stories import AllureStory
from test.tools.allure.tags import AllureTag
from test.tools.assertions.base import assert_status_code
from test.tools.allure.severity import AllureSeverity
from test.tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.NORD_CODES)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.NORD_CODES)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAdditionalFilters:


    @allure.title("[200]OK - Success authorization")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.BLOCKER)
    def test_success_authorization(self, authentication_client: AuthenticationClient):
        query = AuthorizationQuerySchema()
        response = authentication_client.authorization_api(query=query)
        response_data = AuthorizationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())