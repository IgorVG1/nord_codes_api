import pytest
from pydantic import BaseModel

from test.clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from test.clients.authentication.authentication_schema import AuthorizationQuerySchema, AuthorizationResponseSchema
from test.clients.private_http_builder import AuthenticationUserSchema


class UserFixture(BaseModel):
    query: AuthorizationQuerySchema
    response: AuthorizationResponseSchema


    @property
    def username(self) -> str:
        return self.query.username

    @property
    def password(self) -> str:
        return self.query.password

    @property
    def token(self) -> str:
        return self.response.token


    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(username=self.username,
                                        password=self.password)


@pytest.fixture(scope='function')
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture(scope='function')
def function_user(authentication_client: AuthenticationClient) -> UserFixture:
    query = AuthorizationQuerySchema()
    response = authentication_client.authorization(query=query)
    return UserFixture(query=query,
                       response=response)