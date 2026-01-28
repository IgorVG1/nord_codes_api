import pytest, allure

from http import HTTPStatus
from test.clients.logout.logout_client import LogoutClient
from test.clients.logout.logout_schema import LogoutResponseSchema
from test.test_suits.logout.logout_assertions import assert_logout_response
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