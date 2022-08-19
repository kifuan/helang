from helang.lexer import Lexer
from helang.tokens import Token, TokenKind


COMMENTS = """
u8 a = 1 | // Comment inline.
2
// Comment for single line.
"""

OPERATORS = """
a++
a+12
a-b+22
a*b*33
"""


def test_comments():
    lexer = Lexer(COMMENTS)
    tokens = lexer.lex()
    expected = [
        Token('u8', TokenKind.U8),
        Token('a', TokenKind.IDENT),
        Token('=', TokenKind.ASSIGN),
        Token('1', TokenKind.NUMBER),
        Token('|', TokenKind.OR),
        Token('2', TokenKind.NUMBER)
    ]

    assert tokens == expected


def test_operators():
    tokens = Lexer(OPERATORS).lex()
    expected = [
        Token('a', TokenKind.IDENT),
        Token('++', TokenKind.INCREMENT),

        Token('a', TokenKind.IDENT),
        Token('+', TokenKind.ADD),
        Token('12', TokenKind.NUMBER),


        Token('a', TokenKind.IDENT),
        Token('-', TokenKind.SUB),
        Token('b', TokenKind.IDENT),
        Token('+', TokenKind.ADD),
        Token('22', TokenKind.NUMBER),

        Token('a', TokenKind.IDENT),
        Token('*', TokenKind.MUL),
        Token('b', TokenKind.IDENT),
        Token('*', TokenKind.MUL),
        Token('33', TokenKind.NUMBER),
    ]

    assert tokens == expected
