from helang.he_ast import (
    VarExprAST, U8GetAST, U8SetAST
)
from helang.u8 import U8


env = dict()
a = VarExprAST('a')
b = VarExprAST('b')
c = VarExprAST('c')


def setup():
    env['a'] = U8([1, 2, 3, 4])
    env['b'] = U8([1, 3])
    env['c'] = U8([12])


def test_list_get():
    result = U8GetAST(a, b).evaluate(env)
    assert result == [1, 3]


def test_list_set():
    U8SetAST(a, b, c).evaluate(env)
    assert env['a'] == [12, 2, 12, 4]
