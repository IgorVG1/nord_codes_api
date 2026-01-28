from datetime import datetime

from pydantic import BaseModel, Field


class TransactionWithdrawalsRequestSchema(BaseModel):
    """
    Описание структуры запроса на списание средств со счета пользователя.
    Attributes:
        reference_id: str
        amount: float
        description: str
    """
    reference_id: str   = Field(default='reference_id')
    amount: float       = Field(default=100.00)
    description: str    = Field(default='Списание для ставки')


class TransactionWithdrawalsResponseSchema(BaseModel):
    """
    Описание структуры ответа на списание средств со счета пользователя.
    Attributes:
        transaction_id: str
        status: str
        amount: float
        previous_balance: float
        actual_balance: float
        created_at: str
    """
    transaction_id: str
    status: str
    amount: float
    previous_balance: float
    actual_balance: float
    created_at: str


class ErrorTransactionWithdrawalsResponseSchema(BaseModel):
    """
    Описание структуры предупреждения об ошибке списания средств со счета пользователя.
    Attributes:
        error: str
        message: str
        current_balance: str
        required_amount: float
        deficit: float
    """
    error: str = Field(default='Insufficient funds')
    message: str = Field(default='Недостаточно средств на счете')
    current_balance: float
    required_amount: float
    deficit: float


class TransactionDepositsRequestSchema(BaseModel):
    """
    Описание структуры запроса на пополнение счета пользователя.
    Attributes:
        reference_id: str
        payment_method:
        amount: float
        description: str
    """
    reference_id: str       = Field(default='reference_id')
    payment_method: str     = Field(default='credit_card')
    amount: float           = Field(default=100.00)
    description: str        = Field(default='Пополнение счета')


class TransactionDepositsResponseSchema(BaseModel):
    """
    Описание структуры запроса на пополнение счета пользователя.
    Attributes:
        transaction_id: str
        status: str
        amount: float
        payment_method: str
        created_at: str
        previous_balance: float
        actual_balance: float
    """
    transaction_id: str
    status: str
    amount: float
    payment_method: str
    created_at: str
    previous_balance: float
    actual_balance: float