from pydantic import BaseModel, Field
from test.tools.fakers import fake


class CreateTransactionQuerySchema(BaseModel):
    """
    Описание структуры запроса на создание транзакции.
    Attributes:
        action: str - Действие пользователя
        amount: int - Сумма ставки
    """

    action: str         = Field(default='WITHDRAW', description='Действие пользователя')
    amount: int | str   = Field(default_factory=fake.bet, description='Сумма ставки')


class CreateTransactionResponseSchema(BaseModel):
    """
    Описание структуры ответа создания транзакции.
    Attributes:
        result: str - Статус запроса на создание транзакции
        balance: int - Оставшийся баланс пользователя
    """

    result: str     = Field(description='Статус запроса на создание транзакции')
    balance: int    = Field(description='Оставшийся баланс пользователя')


class ErrorCreateTransactionResponseSchema(BaseModel):
    """
    Описание структуры ответа с ошибкой создания транзакции.
    Attributes:
        result: str
        message: str
    """

    result: str
    message: str