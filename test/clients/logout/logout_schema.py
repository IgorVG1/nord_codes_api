from pydantic import BaseModel, Field


class LogoutResponseSchema(BaseModel):
    """
    Описание структуры ответа о завершении сессии.
    Attributes:
        result: str - Статус запроса на завершение сессии
    """

    result: str = Field(description='Статус запроса на завершение сессии')