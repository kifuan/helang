import unittest

from helang.he_ast import VarExprAST, U8GetAST, U8SetAST
from helang.u8 import U8


class TestAST(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Cyber Ding True!')

    def setUp(self) -> None:
        self.env = {'a': U8([1, 2, 3, 4]), 'b': U8([1, 3]), 'c': U8([12])}
        self.a = VarExprAST('a')
        self.b = VarExprAST('b')
        self.c = VarExprAST('c')

    def test_list_get(self):
        result = U8GetAST(self.a, self.b).evaluate(self.env)
        self.assertEqual(result.value, [1, 3])

    def test_list_set(self):
        U8SetAST(self.a, self.b, self.c).evaluate(self.env)
        self.assertEqual(self.env['a'].value, [12, 2, 12, 4])
