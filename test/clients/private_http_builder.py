from functools import lru_cache

from httpx import Client
from pydantic import BaseModel, ConfigDict, Field

from test.clients.authentication.authentication_client import get_authentication_client
from test.clients.authentication.authentication_schema import AuthorizationQuerySchema
from test.clients.event_hooks import log_request_event_hook, log_response_event_hook
from test.config import settings


class AuthenticationUserSchema(BaseModel):
    """
    Структура данных пользователя для авторизации
    Attributes:
        username: str
        password: str
    """
    model_config = ConfigDict(frozen=True)

    username: str   = Field(default=settings.user_data.username)
    password: str   = Field(default=settings.user_data.password)


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с username и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком X-Api-Key.
    """
    authentication_client = get_authentication_client()
    authorization_query = AuthorizationQuerySchema(username=user.username,
                                                   password=user.password)
    authorization_response = authentication_client.authorization(query=authorization_query)

    return Client(
        event_hooks={"request": [log_request_event_hook],
                     "response": [log_response_event_hook]},
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        headers={"Content-Type": "application/x-www-form-urlencoded",
                 "X-Api-Key": f"{authorization_response.token}"}
    )