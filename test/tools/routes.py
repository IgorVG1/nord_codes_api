from enum import Enum


class APIRoutes(str, Enum):
    AUTHENTICATION = '/authorization'
    TRANSACTION = '/transaction'
    LOGOUT = '/logout'

    def __str__(self):
        return self.value