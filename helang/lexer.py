import re

from enum import Enum
from typing import List
from .tokens import Token, TokenKind, SINGLE_CHAR_TOKEN_KINDS, KEYWORD_KINDS
from .exceptions import BadTokenException


class StateSpecificMethods:
    def __init__(self):
        self._methods = dict()

    def bind(self, enum: Enum):
        def bind_method(method: callable):
            self._methods[enum] = method
            return method
        return bind_method

    def apply(self, enum: Enum, *args, **kwargs):
        return self._methods[enum](*args, **kwargs)


class LexerState(Enum):
    # Waiting for next meaningful character.
    WAIT = 1
    # Identifiers.
    IDENT = 2
    # Numbers.
    NUMBER = 3
    # Increments.
    INCREMENT = 4
    # Comments.
    COMMENT = 5


class Lexer:
    _state_methods = StateSpecificMethods()

    def __init__(self, content: str):
        # Add a newline to let the methods do some clean-up.
        self._content = content + '\n'
        self._state = LexerState.WAIT
        self._pos = 0
        self._cache = ''

    def lex(self) -> List[Token]:
        self._pos = 0
        tokens = []
        while self._pos < len(self._content):
            Lexer._state_methods.apply(self._state, self, tokens)
        return tokens

    @property
    def _curr(self):
        """
        Current character.
        :return: current character.
        """
        return self._content[self._pos]

    @_state_methods.bind(LexerState.WAIT)
    def _lex_wait(self, tokens: List[Token]):
        # Anyway, clear the cache.
        self._cache = ''

        if re.match(r'\s', self._curr):
            # Matched space, skipping.
            self._pos += 1
            return

        if self._curr == '/':
            self._state = LexerState.COMMENT
            return

        if re.match(r'\d', self._curr):
            # Matched number, changing state to NUMBER.
            self._state = LexerState.NUMBER
            return

        if re.match(r'[a-zA-Z_$]', self._curr):
            # Matched identifier, changing state to IDENT.
            self._state = LexerState.IDENT
            return

        if self._curr == '+':
            # Matched increment operator, changing state to INCREMENT.
            self._state = LexerState.INCREMENT
            return

        if self._curr in SINGLE_CHAR_TOKEN_KINDS.keys():
            # Matched single char token, adding it to the list.
            kind = SINGLE_CHAR_TOKEN_KINDS[self._curr]
            tokens.append(Token(self._curr, kind))
            self._pos += 1
            return

        raise BadTokenException(self._curr)

    @_state_methods.bind(LexerState.IDENT)
    def _lex_ident(self, tokens: List[Token]):
        if self._cache != '' and not re.match(r'[A-Za-z0-9_$]', self._curr):
            # Current character is not identifier, changing state to WAIT.
            kind = KEYWORD_KINDS.get(self._cache, TokenKind.IDENT)
            tokens.append(Token(self._cache, kind))
            self._state = LexerState.WAIT
            return

        self._cache += self._curr
        self._pos += 1

    @_state_methods.bind(LexerState.NUMBER)
    def _lex_number(self, tokens: List[Token]):
        # Not support for floats yet, as the King He hasn't written any floats.
        if not re.match(r'\d', self._curr):
            # Current character is not number, changing state to WAIT.
            tokens.append(Token(self._cache, TokenKind.NUMBER))
            self._state = LexerState.WAIT
            return

        self._cache += self._curr
        self._pos += 1

    @_state_methods.bind(LexerState.INCREMENT)
    def _lex_increment(self, tokens: List[Token]):
        if self._cache == '+' and self._curr != '+':
            tokens.append(Token('+', TokenKind.ADD))
            self._state = LexerState.WAIT
            return

        if self._cache == '++':
            # Enough + operator, changing state to WAIT.
            tokens.append(Token('++', TokenKind.INCREMENT))
            self._state = LexerState.WAIT
            return

        self._cache += self._curr
        self._pos += 1

    @_state_methods.bind(LexerState.COMMENT)
    def _lex_comment(self, tokens: List[Token]):
        if self._cache == '/' and self._curr != '/':
            raise BadTokenException('/')

        if self._cache == '//':
            if self._curr == '\n':
                self._state = LexerState.WAIT
            self._pos += 1
            return

        self._cache += self._curr
        self._pos += 1
