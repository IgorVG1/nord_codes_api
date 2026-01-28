import uvicorn

from fastapi import FastAPI, HTTPException

from src.schemas.authorization import AuthorizationRequestSchema, AuthorizationResponse200Schema
from src.schemas.logout import LogoutResponse200Schema, LogoutRequestSchema
from src.schemas.transaction import TransactionWithdrawalsRequestSchema, TransactionWithdrawalsResponseSchema, \
    ErrorTransactionWithdrawalsResponseSchema, TransactionDepositsResponseSchema, TransactionDepositsRequestSchema
from test.config import settings

app = FastAPI(title="Corrected REST API for {https://apitests.nyc.wf}",
              version="1.0",
              description=
                  (
                      "Документация для тестового API {https://apitests.nyc.wf} с учетом замечаний и выявленных ошибок"
                  )
              )
@app.post(path='/authorization',
          tags=['Authorization'],
          response_model=AuthorizationResponse200Schema)
def authorization(json: AuthorizationRequestSchema):
    """
    Метод авторизации пользователя.

    :param json: Тело запроса в виде словаря с username и password.
    :return: Ответ в виде JSON.
    """
    if\
            (
            json.username == settings.user_data.username
            and
            json.password == settings.user_data.password
            ):

        return {
            "result": "OK",
            "access_token": "access_token",
            "refresh_token": "refresh_token",
            "balance": 10000
        }

    elif json.username != settings.user_data.username and json.password == settings.user_data.password:
        raise HTTPException(status_code=401,
                            detail="Invalid username")

    elif json.password != settings.user_data.password and json.username == settings.user_data.username:
        raise HTTPException(status_code=401,
                            detail="Invalid password")

    else:
        raise HTTPException(status_code=401,
                            detail="Invalid username or password")


@app.post(path='/transaction/withdrawals',
          tags=['Transaction'],
          response_model=TransactionWithdrawalsResponseSchema)
def withdrawals(json: TransactionWithdrawalsRequestSchema):
    current_balance = 10000.00
    if json.amount <= current_balance:
        return TransactionWithdrawalsResponseSchema(transaction_id=json.reference_id,
                                                    status="Success",
                                                    amount=json.amount,
                                                    previous_balance=current_balance,
                                                    actual_balance=current_balance-json.amount,
                                                    created_at="actual_time").model_dump()
    if json.amount > 10000:
        raise HTTPException(status_code=409,
                            detail="Недостаточно средств")


@app.post(path='/transaction/deposits',
          tags=['Transaction'],
          response_model=TransactionDepositsResponseSchema)
def deposits(json: TransactionDepositsRequestSchema):
    current_balance = 10000.00
    if json.amount <= 0:
        raise HTTPException(status_code=409,
                            detail="Ошибка выполнения транзакции, попробуйте позже.")
    return TransactionDepositsResponseSchema(transaction_id=json.reference_id,
                                             status="Success",
                                             amount=json.amount,
                                             payment_method=json.payment_method,
                                             created_at="actual_time",
                                             previous_balance=current_balance,
                                             actual_balance=current_balance+json.amount).model_dump()


@app.post(path='/logout',
          tags=['Logout'],
          response_model=LogoutResponse200Schema)
def logout(json: LogoutRequestSchema):
    true_access_token = ["access_token", "refresh_token"]
    if json.access_token in true_access_token:
        true_access_token.remove(json.access_token)
        return {
            "session_id": f"{json.session_id}",
            "result": "OK",
            "message": "Session terminated successfully",
        }

    else:
        raise HTTPException(status_code=401,
                            detail="Unauthorized user")


if __name__ == '__main__':
    """
    Для запуска: "python -m src.main"
    
    http://127.0.0.1:8000/docs  - Документация Swagger UI
    """
    uvicorn.run(app="src.main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)