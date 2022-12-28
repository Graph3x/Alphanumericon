from lexer import Lexer
from my_parser import Parser
import sys


def execute(source_code: str, flags: dict) -> None:
    #LEXER
    lexer = Lexer().build_lexer()
    tokens = lexer.lex(source_code)

    if flags['-td']:
        for token in tokens : print(token)
        return

    #PARSER
    pg = Parser()
    pg.parse()
    parser = pg.build_parser()

    for s in parser.parse(tokens):
        s.eval()



def main():

    args = sys.argv[1:]

    source_file = None
    flags ={
        '-td': False,
        '-ti': False,
    }

    for arg in args:
        if arg[0] == '-':
            try:
                flags[arg] = True
            except KeyError:
                print('Invalid flag')
                return
        else:
            source_file = arg
    
    if flags['-ti'] == True:
        source_file = "../test_inputs/test.ano"

    with open(source_file) as f:
        source_code = f.read()

    execute(source_code, flags)


if __name__ == '__main__':
    main()
