from helang.lexer import Lexer
from helang.parser import Parser
from helang.exceptions import BadStatementException, BadTokenException

env = dict()
while True:
    text = input('Speak to Saint He > ')
    lexer = Lexer(text)
    parser = Parser(lexer.lex())
    try:
        parser.parse().evaluate(env)
    except (BadStatementException, BadTokenException) as definedE:
        print(definedE)
        continue
    except Exception:
        print('Error! Revise Saint He\'s videos!')
        continue