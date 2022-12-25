from lexer import Lexer
from my_parser import Parser

test_input = """

print(4 + 4 -2);

"""

lexer = Lexer().build_lexer()
tokens = lexer.lex(test_input)

pg = Parser()
pg.parse()
parser = pg.build_parser()

parser.parse(tokens).eval()