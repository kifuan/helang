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
    SUB = 12
    # ++
    INCREMENT = 13
    # Keywords
    KEYWORD = 14
    # Saint He's U8
    U8 = 15
    # Print statement, supporting for single expression
    PRINT = 16
    # 5G testing statement
    TEST_5G = 17
    # Print string
    SPRINT = 18
    # Whether current region is in the Cyber Spaces.
    CYBERSPACES = 19
    # +
    ADD = 20
    # *
    MUL = 21
    # Print logo.
    LOGO = 22
    # =
    ASSIGN = 23
    # ==
    EQ = 24
    # Less than, <
    LT = 25
    # Greater than, >
    GT = 26
    # Greater than or equals to, >=
    GEQ = 27
    # Less than or equals to, <=
    LEQ = 28
    # Not equals to, !=
    NEQ = 29
    #TEST_5G argument
    T5G_MUSIC = 30
    #TEST_5G argument
    T5G_APP = 31


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
    '-': TokenKind.SUB,
    '*': TokenKind.MUL,
}

KEYWORD_KINDS = {
    'print': TokenKind.PRINT,
    'u8': TokenKind.U8,
    'test5g': TokenKind.TEST_5G,
    'music': TokenKind.T5G_MUSIC,
    'app': TokenKind.T5G_APP,
    'cyberspaces': TokenKind.CYBERSPACES,
    'sprint': TokenKind.SPRINT,
    'logo': TokenKind.LOGO,
}

COMPARATOR_KINDS = {
    '=': TokenKind.ASSIGN,
    '==': TokenKind.EQ,
    '>': TokenKind.GT,
    '>=': TokenKind.GEQ,
    '<': TokenKind.LT,
    '<=': TokenKind.LEQ,
    '!=': TokenKind.NEQ,
}

COMPARATOR_CHARS = {char for op in COMPARATOR_KINDS.keys() for char in op}


class Token:
    def __init__(self, content: str, kind: TokenKind):
        self.content = content
        self.kind = kind

    def __eq__(self, other):
        return self.content == other.content and self.kind == other.kind

    def __repr__(self):
        return f'Token({self.kind}, {self.content})'
