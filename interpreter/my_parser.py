from rply import ParserGenerator
from abstree import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN','SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'STRING', 'VARIABLE', 'SET', 'TRUE', 'FALSE', 'EQL', 'SML', 'BIG', 'SMLQ', 'BIGQ', 'IF', 'INPUT'],
            precedence=[
                ('left', ['VARIABLE',]),
                ('left', ['SET',]),
                ('left', ['IF', 'SEMI_COLON']),
                ('left', ['EQL', 'SML', 'BIG', 'SMLQ', 'BIGQ']),
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV'])
            ]
        )

        self.variables = {}

    def parse(self):

        @self.pg.production('program : statements')
        def program(p):
            return p[0]


        @self.pg.production('statements : statements statement')
        def statements(p):
            if p[1] is None:
                return p[0]
            return p[0] + [p[1]]


        @self.pg.production('statements : statement')
        def statements_stmt(p):
            if p[0] is None:
                return []
            return [p[0]]

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def statement(p):
            return Print(p[2])

        @self.pg.production('statement : VARIABLE SET expression SEMI_COLON')
        def statement(p):
            self.variables[p[0].value] = p[2]

        @self.pg.production('statement : IF expression SEMI_COLON OPEN_PAREN statement CLOSE_PAREN SEMI_COLON')
        def statement(p):
            exp = p[1]
            if exp.eval() == True:
                return p[4]
            else:
                return None

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)

        @self.pg.production('expression : expression EQL expression')
        @self.pg.production('expression : expression BIG expression')
        @self.pg.production('expression : expression SML expression')
        @self.pg.production('expression : expression BIGQ expression')
        @self.pg.production('expression : expression SMLQ expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'EQL':
                return Equals(left, right)
            if operator.gettokentype() == 'BIG':
                return Bigger(left, right)
            if operator.gettokentype() == 'SML':
                return Smaller(left, right)
            if operator.gettokentype() == 'BIGQ':
                return BiggerEqual(left, right)
            if operator.gettokentype() == 'SMLQ':
                return SmallerEqual(left, right)


        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)


        @self.pg.production('expression : STRING')
        def number(p):
            return String(p[0].value[4:-4])

        @self.pg.production('expression : TRUE')
        def number(p):
            return Boolean(p[0].value)

        @self.pg.production('expression : FALSE')
        def number(p):
            return Boolean(p[0].value)

        @self.pg.production('expression : VARIABLE')
        def handle_var(p):
            return self.variables[p[0].value]


        @self.pg.production('expression : INPUT')
        def handle_var(p):
            return Input()


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)


    def build_parser(self):
        return self.pg.build()