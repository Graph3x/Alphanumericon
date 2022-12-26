from rply import ParserGenerator
from abstree import Number, Sum, Sub, Print, Mul, Div, String, StringVar


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN','SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'STRING', 'VARIABLE', 'SET'],
            precedence=[('left', ['PLUS', 'MINUS']), ('left', ['MUL', 'DIV'])]
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


        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)


        @self.pg.production('expression : STRING')
        def number(p):
            return String(p[0].value[4:-4])


        @self.pg.production('expression : VARIABLE')
        def handle_var(p):
            return self.variables[p[0].value]


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)


    def build_parser(self):
        return self.pg.build()