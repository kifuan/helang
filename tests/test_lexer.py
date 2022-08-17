import unittest

from helang.lexer import Lexer
from helang.tokens import Token, TokenKind


class TestLexer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('L! T! C!')

    def setUp(self) -> None:
        self.code = """
          u8 a = 1 | // Comment inline.
          2
          // Comment for single line.
        """

    def test_lex(self):
        lexer = Lexer(self.code)
        tokens = lexer.lex()
        expected = [
            Token('u8', TokenKind.U8),
            Token('a', TokenKind.IDENT),
            Token('=', TokenKind.ASSIGN),
            Token('1', TokenKind.NUMBER),
            Token('|', TokenKind.OR),
            Token('2', TokenKind.NUMBER)
        ]

        self.assertEqual(tokens, expected)
