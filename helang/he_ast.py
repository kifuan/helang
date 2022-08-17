import random

from typing import Dict, Optional, List
from .u8 import U8
from .speed_tester import run_speed_test
from .exceptions import CyberNameException


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


class SubtractionAST(AST):
    def __init__(self, first: AST, second: AST):
        self._first = first
        self._second = second

    def evaluate(self, env: Dict[str, U8]) -> U8:
        first = self._first.evaluate(env)
        second = self._second.evaluate(env)
        return first - second


class ListAST(AST):
    def __init__(self, asts: List[AST]):
        self.asts = asts

    def evaluate(self, env: Dict[str, U8]) -> U8:
        last = U8()
        for ast in self.asts:
            last = ast.evaluate(env)
        return last


class VoidAST(AST):
    def evaluate(self, env: Dict[str, U8]) -> U8:
        return U8()


class U8SetAST(AST):
    def __init__(self, list_expr: AST, subscript_expr: AST, value_expr: AST):
        self._list = list_expr
        self._subscript = subscript_expr
        self._value = value_expr

    def evaluate(self, env: Dict[str, U8]) -> U8:
        lst = self._list.evaluate(env).value
        subscripts = self._subscript.evaluate(env).value
        val = self._value.evaluate(env).value
        # Flat single element list to the element itself.
        if len(val) == 1:
            val = val[0]
        for i in subscripts:
            # Saint He likes arrays whose subscript start from 1.
            lst[i-1] = val
        return U8()


class U8GetAST(AST):
    def __init__(self, list_expr: AST, subscript_expr: AST):
        self._list = list_expr
        self._subscript = subscript_expr

    def evaluate(self, env: Dict[str, U8]) -> U8:
        lst = self._list.evaluate(env).value
        subscripts = self._subscript.evaluate(env).value
        # Like the operation of sublist.
        # And Saint He likes arrays whose subscript start from 1.
        return U8([lst[i-1] for i in range(1, len(lst) + 1) if i in subscripts])


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
