import enum


class TokenKind(enum.Enum):
    # Numbers like 123, 276, etc.
    NUMBER = 1
    # |
    OR = 2
    # Identifiers
    IDENT = 3
    # (
    LP = 4
    # )
    RP = 5
    # {
    LC = 6
    # }
    RC = 7
    # [
    LS = 8
    # ]
    RS = 9
    # ,
    COMMA = 10
    # ;
    SEMICOLON = 11
    # -
    MINUS = 12
    # ++
    INCREMENT = 13
    # =
    ASSIGN = 14
    # Less than, <
    LT = 15
    # Keywords
    KEYWORD = 16
    # Saint He's U8
    U8 = 17
    # Print statement, supporting for single expression
    PRINT = 18


SINGLE_CHAR_TOKEN_KINDS = {
    '|': TokenKind.OR,
    '(': TokenKind.LP,
    ')': TokenKind.RP,
    '{': TokenKind.LC,
    '}': TokenKind.RC,
    '[': TokenKind.LS,
    ']': TokenKind.RS,
    ',': TokenKind.COMMA,
    ';': TokenKind.SEMICOLON,
    '=': TokenKind.ASSIGN,
    '<': TokenKind.LT,
    '-': TokenKind.MINUS,
}


class Token:
    def __init__(self, content: str, kind: TokenKind):
        self.content = content
        self.kind = kind

    def __eq__(self, other):
        return self.content == other.content and self.kind == other.kind