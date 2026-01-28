from enum import Enum


class AllureFeature(str, Enum):

    AUTHENTICATION = "AUTHENTICATION"
    TRANSACTION = "TRANSACTION"
    LOGOUT = "LOGOUT"