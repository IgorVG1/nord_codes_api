from pydantic import BaseModel, Field
from test.config import settings


class AuthorizationQuerySchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    Attributes:
        username: str
        password: str
    """
    username: str   = Field(default=settings.user_data.username)
    password: str   = Field(default=settings.user_data.password)


class AuthorizationResponseSchema(BaseModel):
    """
    Описание структуры ответа на успешную аутентификацию.
    Attributes:
        result: str
        token: str
        balance: int
    """
    result: str
    token: str
    balance: int