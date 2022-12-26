from lexer import Lexer
from my_parser import Parser
from codegen import CodeGen


def main():
    source_file = "test.ano"

    with open(source_file) as f:
        source_code = f.read()

    #LEXER
    lexer = Lexer().build_lexer()
    tokens = lexer.lex(source_code)

    #CODEGEN - DECLARATION
    codegen = CodeGen()

    #PARSER
    pg = Parser(codegen.module, codegen.builder, codegen.printf)
    pg.parse()
    parser = pg.build_parser()

    parser.parse(tokens).eval()

    #CODEGEN GENERATION
    codegen.create_ir()
    output_file = source_file[:-3] + "ll"
    codegen.save_ir(output_file)



if __name__ == '__main__':
    main()
