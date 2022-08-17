import unittest

from helang.parser import Parser
from helang.lexer import Lexer
from helang.u8 import U8
from helang.he_ast import Test5GAST, AST
from helang.speed_tester import MUSICS


def parse(code: str) -> AST:
    return Parser(Lexer(code).lex()).parse()


class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('1! 5! 哥们在这给你测试!')

    def setUp(self) -> None:
        self.def_code = """
            u8 list1 = 1 | 2 | 3;
            u8 list2 = [3];
        """

        self.u8_set_code = """
            u8 a = 1 | 2 | 3;
            a[1 | 3] = 12;
        """

        # You need to provide variable a.
        self.u8_get_code = """
            u8 b = a[1 | 3];
        """

        # You need to provide variable a.
        self.print_code = """
            print a[1 | 2];
        """

        self.test_5g_code = """
            test5g;
        """

        self.decl_code = """
            u8 a;
        """

        self.var_assign_code = """
            u8 a = 1 | 2;
            a = 3 | 4;
        """

        self.var_increment_code = """
            u8 a = 1 | 2 | 3;
            a++;
        """

        self.env = dict()

    def test_parse_def(self):
        lexer = Lexer(self.def_code)
        Parser(lexer.lex()).parse().evaluate(self.env)
        self.assertEqual(self.env['list1'].value, [1, 2, 3])
        self.assertEqual(self.env['list2'].value, [0, 0, 0])

    def test_parse_u8_set(self):
        parse(self.u8_set_code).evaluate(self.env)
        self.assertEqual(self.env['a'].value, [12, 2, 12])

    def test_parse_u8_get(self):
        self.env['a'] = U8([2, 3, 4])
        parse(self.u8_get_code).evaluate(self.env)
        self.assertEqual(self.env['b'].value, [2, 4])

    def test_parse_print(self):
        self.env['a'] = U8([2, 3, 4])
        printed_content = parse(self.print_code).evaluate(self.env)
        self.assertEqual(printed_content.value, [2, 3])

    def test_parse_test_5g(self):
        # Hack the testing musics to reduce time.
        MUSICS.clear()
        MUSICS.append('TEST')
        result = parse(self.test_5g_code).evaluate(self.env)
        self.assertEqual(result.value, Test5GAST.SPECIAL_VALUE)

    def test_parse_decl(self):
        parse(self.decl_code).evaluate(self.env)
        self.assertEqual(self.env['a'].value, [])

    def test_parse_var_assign(self):
        parse(self.var_assign_code).evaluate(self.env)
        self.assertEqual(self.env['a'].value, [3, 4])

    def test_parse_increment(self):
        parse(self.var_increment_code).evaluate(self.env)
        self.assertEqual(self.env['a'].value, [2, 3, 4])
