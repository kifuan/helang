import sys
import threading

from ..lexer import Lexer
from ..parser import Parser
from ..exceptions import HeLangException
from typing import TextIO


class Runner(threading.Thread):
    def __init__(self, code: str, stdout: TextIO):
        super().__init__()
        self.code = code
        self.stdout = stdout

    def run(self):
        raw_stdout = sys.stdout
        sys.stdout = self.stdout

        try:
            Parser(Lexer(self.code).lex()).parse().evaluate(dict())
        except HeLangException as e:
            print(f'{type(e).__name__}: {e}')

        sys.stdout = raw_stdout
