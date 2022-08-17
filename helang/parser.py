from .tokens import Token, TokenKind
from .exceptions import BadStatementException
from .he_ast import AST, VoidAST, ListAST, VarDefAST, VarAssignAST, VarExprAST,\
    PrintAST, SprintAST, VarIncrementAST, U8SetAST, U8GetAST, Test5GAST,\
    EmptyU8InitAST, OrU8InitAST
from typing import List, Optional, Callable, Tuple


class Parser:
    def __init__(self, tokens: List[Token]):
        self._tokens = tokens
        self._pos = 0

    def _expect(self, expected_kind: TokenKind, validator: Optional[Callable[[Token], bool]] = None):
        if self._pos >= len(self._tokens):
            raise BadStatementException('no more tokens')

        token = self._tokens[self._pos]

        if token.kind != expected_kind:
            raise BadStatementException(f'expected {expected_kind} at pos {self._pos}, got {token.kind}')

        if validator is not None and not validator(token):
            raise BadStatementException(f'failed to pass custom validator at offset {self._pos}')

        self._pos += 1
        return token

    def parse(self) -> AST:
        root_parsers = [
            self._root_parse_print,
            self._root_parse_sprint,
            self._root_parse_u8_set,
            self._root_parse_var_def,
            self._root_parse_var_declare,
            self._root_parse_var_assign,
            self._root_parse_var_increment,
            self._root_parse_expr,
            self._root_parse_test_5g,
        ]
        asts = []
        while self._pos < len(self._tokens):
            for parser in root_parsers:
                saved_pos = self._pos
                try:
                    asts.append(parser())
                    break
                except BadStatementException:
                    self._pos = saved_pos
            else:
                raise BadStatementException(f'failed to parse tokens started from {self._pos}, '
                                            f'which is {self._tokens[self._pos]}')
        return ListAST(asts)

    def _root_parse_var_def(self) -> AST:
        self._expect(TokenKind.U8)
        var_ident = self._expect(TokenKind.IDENT)
        self._expect(TokenKind.ASSIGN)
        val = self._root_parse_expr()
        self._expect(TokenKind.SEMICOLON)
        return VarDefAST(var_ident.content, val)

    def _root_parse_var_declare(self) -> AST:
        self._expect(TokenKind.U8)
        var_ident = self._expect(TokenKind.IDENT)
        self._expect(TokenKind.SEMICOLON)
        return VarDefAST(var_ident.content, VoidAST())

    def _root_parse_var_assign(self) -> AST:
        ident = self._expect(TokenKind.IDENT)
        self._expect(TokenKind.ASSIGN)
        expr = self._root_parse_expr()
        self._expect(TokenKind.SEMICOLON)
        return VarAssignAST(ident.content, expr)

    def _root_parse_print(self) -> AST:
        self._expect(TokenKind.PRINT)
        expr = self._root_parse_expr()
        self._expect(TokenKind.SEMICOLON)
        return PrintAST(expr)

    def _root_parse_sprint(self) -> AST:
        self._expect(TokenKind.SPRINT)
        expr = self._root_parse_expr()
        self._expect(TokenKind.SEMICOLON)
        return SprintAST(expr)

    def _root_parse_var_increment(self) -> AST:
        ident = self._expect(TokenKind.IDENT)
        self._expect(TokenKind.INCREMENT)
        self._expect(TokenKind.SEMICOLON)
        return VarIncrementAST(ident.content)

    def _root_parse_test_5g(self) -> AST:
        self._expect(TokenKind.TEST_5G)
        self._expect(TokenKind.SEMICOLON)
        return Test5GAST()

    def _root_parse_u8_set(self) -> U8SetAST:
        list_expr, subscript_expr = self._parse_u8_common_parts()
        self._expect(TokenKind.RS)
        self._expect(TokenKind.ASSIGN)
        value_expr = self._root_parse_expr()
        self._expect(TokenKind.SEMICOLON)
        return U8SetAST(list_expr, subscript_expr, value_expr)

    def _root_parse_expr(self, skip_u8=False) -> AST:
        expr_parsers = [self._parse_empty_u8_expr, self._parse_or_u8_expr, self._parse_u8_get, self._parse_var_expr]
        for parser in expr_parsers:
            if skip_u8 and parser == self._parse_u8_get:
                continue
            saved_pos = self._pos
            try:
                return parser()
            except BadStatementException:
                self._pos = saved_pos
        raise BadStatementException('cannot parse expressions')

    def _parse_empty_u8_expr(self) -> AST:
        self._expect(TokenKind.LS)
        length = self._expect(TokenKind.NUMBER)
        self._expect(TokenKind.RS)
        return EmptyU8InitAST(int(length.content))

    def _parse_or_u8_expr(self) -> OrU8InitAST:
        first = self._expect(TokenKind.NUMBER)

        try:
            self._expect(TokenKind.OR)
        except BadStatementException:
            return OrU8InitAST(int(first.content))

        return OrU8InitAST(int(first.content), self._parse_or_u8_expr())

    def _parse_var_expr(self) -> VarExprAST:
        ident = self._expect(TokenKind.IDENT)
        return VarExprAST(ident.content)

    def _parse_u8_get(self) -> U8GetAST:
        list_expr, subscript_expr = self._parse_u8_common_parts()
        self._expect(TokenKind.RS)
        return U8GetAST(list_expr, subscript_expr)

    def _parse_u8_common_parts(self) -> Tuple[AST, AST]:
        list_expr = self._root_parse_expr(skip_u8=True)
        self._expect(TokenKind.LS)
        subscript_expr = self._root_parse_expr()
        return list_expr, subscript_expr
