import enum

from typing import Dict, Optional, List, Union
from .u8 import U8
from .check_cyberspaces import check_cyberspaces
from .speed_tester import run_speed_test_music, run_speed_test_app
from .logo import print_logo
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


class Test5GMusicAST(AST):
    def evaluate(self, env: Dict[str, U8]) -> U8:
        run_speed_test_music()
        return U8()


class Test5GAppAST(AST):
    def evaluate(self, env: Dict[str, U8]) -> U8:
        run_speed_test_app()
        return U8()


class LogoSize(enum.Enum):
    TINY = 100
    MEDIUM = 130
    LARGE = 180

    @classmethod
    def from_token(cls, token: Token):
        operators = {
            TokenKind.LOGO_TINY: cls.TINY,
            TokenKind.LOGO_MEDIUM: cls.MEDIUM,
            TokenKind.LOGO_LARGE: cls.LARGE,
        }
        return operators[token.kind]


class LogoAST(AST):
    def __init__(self, size: LogoSize):
        self._size = size

    def evaluate(self, env: Dict[str, U8]) -> U8:
        print_logo(self._size)
        return U8()


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


class Operator(enum.Enum):
    LT = 1
    LEQ = 2
    GT = 3
    GEQ = 4
    EQ = 5
    NEQ = 6
    ADD = 7
    SUB = 8
    MUL = 9

    @property
    def priority(self):
        mapping = {
            Operator.LT: 0,
            Operator.LEQ: 0,
            Operator.GT: 0,
            Operator.GEQ: 0,
            Operator.EQ: 0,
            Operator.NEQ: 0,
            Operator.ADD: 1,
            Operator.SUB: 1,
            Operator.MUL: 2,
        }
        return mapping[self]

    def operate(self, a: U8, b: U8) -> U8:
        operation = {
            Operator.LT: a.__lt__,
            Operator.LEQ: a.__le__,
            Operator.GT: a.__gt__,
            Operator.GEQ: a.__ge__,
            Operator.EQ: a.__eq__,
            Operator.NEQ: lambda n: not a.__eq__(n),
            Operator.ADD: a.__add__,
            Operator.SUB: a.__sub__,
            Operator.MUL: a.__mul__,
        }
        result = operation[self](b)
        return result if not isinstance(result, bool) else U8(int(result))

    @classmethod
    def from_token(cls, token: Token):
        operators = {
            TokenKind.ADD: cls.ADD,
            TokenKind.SUB: cls.SUB,
            TokenKind.MUL: cls.MUL,
            TokenKind.LT: cls.LT,
            TokenKind.LEQ: cls.LEQ,
            TokenKind.GT: cls.GT,
            TokenKind.GEQ: cls.GEQ,
            TokenKind.EQ: cls.EQ,
            TokenKind.NEQ: cls.NEQ,
        }
        return operators[token.kind]


def _calc(nums: List[U8], ops: List[Operator]):
    if len(nums) < 2:
        return
    if not ops:
        return
    b = nums.pop()
    a = nums.pop()
    op = ops.pop()
    nums.append(op.operate(a, b))


class OperationAST(AST):
    def __init__(self, first: AST, second: AST, op: Operator):
        self._first = first
        self._second = second
        self._op = op

    # https://leetcode.cn/problems/basic-calculator-ii/solution/dai-ma-jian-ji-yi-chong-huan-bu-cuo-de-j-nhrq/
    def evaluate(self, env: Dict[str, U8]) -> U8:
        expr = self._to_expression(env)
        nums = []
        ops = []
        for item in expr:
            if isinstance(item, U8):
                nums.append(item)
                continue

            while ops:
                prev = ops[-1]
                if prev.priority >= item.priority:
                    _calc(nums, ops)
                else:
                    break
            ops.append(item)

        while ops:
            _calc(nums, ops)
        return nums[-1]

    def _to_expression(self, env: Dict[str, U8]) -> List[Union[U8, Operator]]:
        expr = []

        if isinstance(self._first, OperationAST):
            expr.extend(self._first._to_expression(env))
        else:
            expr.append(self._first.evaluate(env))

        expr.append(self._op)

        if isinstance(self._second, OperationAST):
            expr.extend(self._second._to_expression(env))
        else:
            expr.append(self._second.evaluate(env))

        return expr
