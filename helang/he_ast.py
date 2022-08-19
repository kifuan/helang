import enum
import random

from typing import Dict, Optional, List, Tuple
from .u8 import U8
from .check_cyberspaces import check_cyberspaces
from .speed_tester import run_speed_test
from .exceptions import CyberNameException
from .tokens import Token, TokenKind


class AST:
    def evaluate(self, env: Dict[str, U8]) -> U8:
        raise NotImplementedError()


class VarDefAST(AST):
    def __init__(self, ident: str, val: AST):
        self._ident = ident
        self._val = val

    def evaluate(self, env: Dict[str, U8]) -> U8:
        val = self._val.evaluate(env)
        env[self._ident] = val
        return U8()


class VarAssignAST(AST):
    def __init__(self, ident: str, val: AST):
        self._ident = ident
        self._val = val

    def evaluate(self, env: Dict[str, U8]) -> U8:
        if self._ident not in env.keys():
            raise CyberNameException(f'{self._ident} is not defined.')
        val = self._val.evaluate(env)
        env[self._ident] = val
        return val


class VarIncrementAST(AST):
    def __init__(self, ident: str):
        self._ident = ident

    def evaluate(self, env: Dict[str, U8]) -> U8:
        var = env[self._ident]
        var.increment()
        return var


class VarExprAST(AST):
    def __init__(self, ident: str):
        self._ident = ident

    def evaluate(self, env: Dict[str, U8]) -> U8:
        if self._ident not in env.keys():
            raise CyberNameException(f'{self._ident} is not defined.')
        return env[self._ident]


class EmptyU8InitAST(AST):
    def __init__(self, length: int):
        self._length = length

    def evaluate(self, env: Dict[str, U8]) -> U8:
        return U8([0] * self._length)


class OrU8InitAST(AST):
    """
    How the King He defines uint8 list: by | operator.
    """

    def __init__(self, first: int, second: Optional['OrU8InitAST'] = None):
        self._first = first
        self._second = second

    def evaluate(self, env: Dict[str, U8]) -> U8:
        if self._second is None:
            return U8([self._first])
        second = self._second.evaluate(env).value
        elements = [self._first]
        elements.extend(second)
        return U8(elements)


class ListAST(AST):
    def __init__(self, asts: List[AST]):
        self.asts = asts

    def evaluate(self, env: Dict[str, U8]) -> U8:
        for ast in self.asts:
            ast.evaluate(env)
        return U8()


class VoidAST(AST):
    def evaluate(self, env: Dict[str, U8]) -> U8:
        return U8()


class U8SetAST(AST):
    def __init__(self, list_expr: AST, subscript_expr: AST, value_expr: AST):
        self._list = list_expr
        self._subscript = subscript_expr
        self._value = value_expr

    def evaluate(self, env: Dict[str, U8]) -> U8:
        lst = self._list.evaluate(env)
        subscripts = self._subscript.evaluate(env)
        val = self._value.evaluate(env)
        lst[subscripts] = val
        return U8()


class U8GetAST(AST):
    def __init__(self, list_expr: AST, subscript_expr: AST):
        self._list = list_expr
        self._subscript = subscript_expr

    def evaluate(self, env: Dict[str, U8]) -> U8:
        lst = self._list.evaluate(env)
        subscripts = self._subscript.evaluate(env)
        return lst[subscripts]


class PrintAST(AST):
    def __init__(self, expr: AST):
        self._expr = expr

    def evaluate(self, env: Dict[str, U8]) -> U8:
        val = self._expr.evaluate(env)
        print(str(val))
        return val


class Test5GAST(AST):
    # To avoid coincidence.
    SPECIAL_VALUE = [random.randint(1, 100), random.randint(1, 100)]

    def evaluate(self, env: Dict[str, U8]) -> U8:
        run_speed_test()
        return U8(Test5GAST.SPECIAL_VALUE)


class SprintAST(AST):
    def __init__(self, expr: AST):
        self._expr = expr

    def evaluate(self, env: Dict[str, U8]) -> U8:
        chars = self._expr.evaluate(env)
        val = ''.join(chr(char) for char in chars.value)
        print(val)
        return chars


class CyberspacesAST(AST):
    def evaluate(self, env: Dict[str, U8]) -> U8:
        check_cyberspaces()
        return U8()


class ArithmeticOperator(enum.Enum):
    ADD = 1
    SUB = 2
    MUL = 3

    @classmethod
    def from_token(cls, token: Token):
        operators = {
            TokenKind.ADD: cls.ADD,
            TokenKind.SUB: cls.SUB,
            TokenKind.MUL: cls.MUL
        }
        return operators[token.kind]


def _operate(a: U8, b: U8, op: ArithmeticOperator):
    if op == ArithmeticOperator.SUB:
        return a - b
    elif op == ArithmeticOperator.ADD:
        return a + b
    elif op == ArithmeticOperator.MUL:
        return a * b
    else:
        raise NotImplementedError()


class ArithmeticAST(AST):
    def __init__(self, first: AST, second: AST, op: ArithmeticOperator):
        self._first = first
        self._second = second
        self._op = op

    def evaluate(self, env: Dict[str, U8]) -> U8:
        # TODO multiplication and division.
        asts, operators = self._expand()
        u8s = [ast.evaluate(env) for ast in asts]
        while len(u8s) > 1:
            first = u8s.pop(0)
            second = u8s.pop(0)
            op = operators.pop(0)
            result = _operate(first, second, op)
            u8s.insert(0, result)
        return u8s[0]

    def _expand(self) -> Tuple[List[AST], List[ArithmeticOperator]]:
        asts = []
        operators = []

        if isinstance(self._first, ArithmeticAST):
            asts_second, operators_second = self._first._expand()
            asts.extend(asts_second)
            operators.extend(operators_second)
        else:
            asts.append(self._first)

        operators.append(self._op)

        if isinstance(self._second, ArithmeticAST):
            asts_second, operators_second = self._second._expand()
            asts.extend(asts_second)
            operators.extend(operators_second)
        else:
            asts.append(self._second)

        return asts, operators
