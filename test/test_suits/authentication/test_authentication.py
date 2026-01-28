import allure, pytest
from http import HTTPStatus

from test.clients.authentication.authentication_client import AuthenticationClient
from test.clients.authentication.authentication_schema import AuthorizationQuerySchema, AuthorizationResponseSchema, \
    InvalidAuthorizationResponseSchema
from test.test_suits.authentication.authentication_assertions import \
    assert_invalid_authorization_response_with_incorrect_data, \
    assert_invalid_authorization_response_with_empty_username, \
    assert_invalid_authorization_response_with_empty_password, assert_invalid_authorization_response_with_empty_data
from test.test_suits.authentication.data import USERNAME_403, USERNAME_400, PASSWORDS_400, PASSWORDS_403
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


    @pytest.mark.parametrize('username_403',USERNAME_403)
    @allure.title("[403]FORBIDDEN - Invalid authorization with incorrect username")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_invalid_authorization_with_incorrect_username(self,username_403: str, authentication_client: AuthenticationClient):
        query = AuthorizationQuerySchema(username=username_403)
        response = authentication_client.authorization_api(query=query)
        response_data = InvalidAuthorizationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)
        assert_invalid_authorization_response_with_incorrect_data(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.parametrize('username_400',USERNAME_400)
    @allure.title("[400]BAD_REQUEST - Invalid authorization with empty username")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_invalid_authorization_with_empty_username(self,username_400: str, authentication_client: AuthenticationClient):
        query = AuthorizationQuerySchema(username=username_400)
        response = authentication_client.authorization_api(query=query)
        response_data = InvalidAuthorizationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_invalid_authorization_response_with_empty_username(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.parametrize('password_403',PASSWORDS_403)
    @allure.title("[403]FORBIDDEN - Invalid authorization with incorrect password")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_invalid_authorization_with_incorrect_password(self, password_403: str, authentication_client: AuthenticationClient):
        query = AuthorizationQuerySchema(password=password_403)
        response = authentication_client.authorization_api(query=query)
        response_data = InvalidAuthorizationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)
        assert_invalid_authorization_response_with_incorrect_data(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @pytest.mark.parametrize('password_400',USERNAME_400)
    @allure.title("[400]BAD_REQUEST - Invalid authorization with empty password")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_invalid_authorization_with_empty_password(self,password_400: str, authentication_client: AuthenticationClient):
        query = AuthorizationQuerySchema(password=password_400)
        response = authentication_client.authorization_api(query=query)
        response_data = InvalidAuthorizationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_invalid_authorization_response_with_empty_password(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())


    @allure.title("[400]BAD_REQUEST - Invalid authorization with empty data")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(AllureSeverity.MAJOR)
    def test_invalid_authorization_with_empty_data(self, authentication_client: AuthenticationClient):
        query = AuthorizationQuerySchema(username='',
                                         password="")
        response = authentication_client.authorization_api(query=query)
        response_data = InvalidAuthorizationResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_invalid_authorization_response_with_empty_data(response=response_data)
        validate_json_schema(instance=response.json(),
                             schema=response_data.model_json_schema())