from lexer import Lexer
from my_parser import Parser


def main():
    source_file = "../test_inputs/test.ano"

    with open(source_file) as f:
        source_code = f.read()

    #LEXER
    lexer = Lexer().build_lexer()
    tokens = lexer.lex(source_code)

    #PARSER
    pg = Parser()
    pg.parse()
    parser = pg.build_parser()

    for s in parser.parse(tokens):
        s.eval()

if __name__ == '__main__':
    main()
