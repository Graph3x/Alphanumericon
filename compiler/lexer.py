from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()


    def add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'PRINT')
        # Parenthesis open and closed
        self.lexer.add('OPEN_PAREN', r'sI')
        self.lexer.add('CLOSE_PAREN', r'Is')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'e')
        # Plus and minus
        self.lexer.add('SUM', r'plus')
        self.lexer.add('SUB', r'minus')
        # Numbers
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')


    def build_lexer(self):
        self.add_tokens()
        return self.lexer.build()
