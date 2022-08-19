from typing import Dict, Optional
from .lexer import Lexer
from .parser import Parser
from .u8 import U8


def quick_run_file(path: str, env: Optional[Dict[str, U8]] = None):
    """
    Runs HeLang file quickly.
    :param path: the path to file.
    :param env: optional environment, we will use it if you specify.
    """

    with open(path, 'r') as f:
        code = f.read()
    quick_run_string(code, env)


def quick_run_string(code: str, env: Optional[Dict[str, U8]] = None):
    """
    Runs HeLang code in string quickly.
    :param code: the HeLang code.
    :param env: optional environment, we will use it if you specify.
    """
    tokens = Lexer(code).lex()
    ast = Parser(tokens).parse()
    if env is None:
        env = dict()
    ast.evaluate(env)
