from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        checkReservedWordEnd = r"(?!\w)"
        # Logical Operators
        self.lexer.add("AND", r"e" + checkReservedWordEnd)
        self.lexer.add("OR", r"o" + checkReservedWordEnd)
        self.lexer.add("EQUAL", r"\=\=")
        self.lexer.add("NOT_EQUAL", r"\!\=")
        self.lexer.add("BIGGER_EQ", r"\>\=")
        self.lexer.add("BIGGER", r"\>")
        self.lexer.add("SMALLER_EQ", r"\<\=")
        self.lexer.add("SMALLER", r"\<")
        # Assignment
        self.lexer.add("ASSIGN", r"\=")
        # Function
        self.lexer.add("DEF_FUNC", r"funzione" + checkReservedWordEnd)
        self.lexer.add("RETURN", r"ritorna" + checkReservedWordEnd)
        self.lexer.add("COMMA", r"\,")
        # If/Else, while, for
        self.lexer.add("IF", r"se" + checkReservedWordEnd)
        self.lexer.add("ELSE", r"altro" + checkReservedWordEnd)
        self.lexer.add("WHILE", r"mentre" + checkReservedWordEnd)
        self.lexer.add("FOR", r"per" + checkReservedWordEnd)
        # Binary and Unary Operators
        self.lexer.add("PLUS", r"\+")
        self.lexer.add("MINUS", r"\-")
        self.lexer.add("MULT", r"\*")
        self.lexer.add("DIV", r"\/")
        self.lexer.add("NOT", r"non" + checkReservedWordEnd)
        # Print
        self.lexer.add("PRINT", r"stampa" + checkReservedWordEnd)
        # Input
        self.lexer.add("READ", r"leggere" + checkReservedWordEnd)
        # Identifier
        self.lexer.add("IDENTIFIER", r"[a-zA-Z][a-zA-Z0-9_]*")
        # Number
        self.lexer.add("INTEGER", r"\d+")
        # Parenthesis
        self.lexer.add("OPEN_PAR", r"\(")
        self.lexer.add("CLOSE_PAR", r"\)")
        # Brackets
        self.lexer.add("OPEN_BRACKET", r"\{")
        self.lexer.add("CLOSE_BRACKET", r"\}")
        # Semicolon
        self.lexer.add("SEMICOLON", r"\;")
        # Spaces
        self.lexer.ignore("\s+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
