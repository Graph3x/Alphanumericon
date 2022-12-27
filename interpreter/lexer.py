from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()


    def add_tokens(self):
        # BUILD IN FUNCTIONS
        self.lexer.add('PRINT', r'PRINT')

        # SEPERATORS
        self.lexer.add('OPEN_PAREN', r'iI')
        self.lexer.add('CLOSE_PAREN', r'Ii')

        # MATH SYMBOLS
        self.lexer.add('SUM', r'plus')
        self.lexer.add('SUB', r'minus')
        self.lexer.add('MUL', r'times')
        self.lexer.add('DIV', r'divided')

        self.lexer.add('EQL', r'equals')
        self.lexer.add('SMLQ', r'smallerq')
        self.lexer.add('BIGQ', r'biggerq')
        self.lexer.add('SML', r'smaller')
        self.lexer.add('BIG', r'bigger')
        

        # DATA TYPES
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('STRING', r"stI(?:(?!stI).)*stI")
        self.lexer.add('TRUE', r"TRUE")
        self.lexer.add('FALSE', r"FALSE")

        #LOGIC AND LOOPS
        self.lexer.add('IF', 'IF')

        #USE SEMICOLONS
        self.lexer.add('SEMI_COLON', r'e')

        # VARS
        self.lexer.add('SET', r'SET')
        self.lexer.add('VARIABLE', r'[^\s]+')

        # IGNORE SPACES
        self.lexer.ignore('\s+')


    def build_lexer(self):
        self.add_tokens()
        return self.lexer.build()