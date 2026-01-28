from pydantic import BaseModel, Field


class AuthorizationRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    Attributes:
        username: str
        password: str
    """
    username: str = Field(default='admin')
    password: str = Field(default='qazWSXedc')


class AuthorizationResponse200Schema(BaseModel):
    """
    Описание структуры [200] ответа на успешную аутентификацию.
    Attributes:
        result: str
        access_token: str
        refresh_token: str
        balance: int
    """
    result: str
    access_token: str
    refresh_token: str
    balance: int