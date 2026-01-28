from pydantic import BaseModel, Field


class LogoutRequestSchema(BaseModel):
    """
    Описание структуры запроса на завершение сессии.
    Attributes:
        access_token: str
        session_id: int
    """
    access_token: str   = Field(default='access_token')
    session_id: int     = Field(default=1)


class LogoutResponse200Schema(BaseModel):
    """
    Описание структуры [200] ответа на успешное завершение сессии.
    Attributes:
        session_id: int
        result: str
        message: str
    """
    session_id: int
    result: str
    message: str