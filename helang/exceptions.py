class HeLangException(Exception):
    ...


class BadTokenException(HeLangException):
    ...


class BadStatementException(HeLangException):
    ...


class CyberNameException(HeLangException):
    ...


class CyberArithmeticException(HeLangException):
    ...


class CyberU8ComparingException(HeLangException):
    ...


class CyberNotSupportedException(HeLangException):
    ...


class CyberNetworkException(HeLangException):
    ...
