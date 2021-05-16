from rply import ParserGenerator, Token
from components.node import (
    BinOp,
    IntVal,
    UnOp,
    Identifier,
    Assign,
    NoOp,
    Block,
    Print,
    Read,
    LogicalOp,
    While,
    If,
    For,
    Declare,
)
from components.symbolTable import SymbolTable


ALPHABET = [
    # Logical Operators
    "AND",
    "OR",
    "EQUAL",
    "NOT_EQUAL",
    "BIGGER_EQ",
    "BIGGER",
    "SMALLER_EQ",
    "SMALLER",
    # Assignment
    "ASSIGN",
    # Function
    "DEF_FUNC",
    "RETURN",
    "COMMA",
    # If/Else, While, for
    "IF",
    "ELSE",
    "WHILE",
    "FOR",
    # Binary and Unary Operators
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "NOT",
    # Print
    "PRINT",
    # Input
    "READ",
    # Number
    "INTEGER",
    # Identifier
    "VAR",
    "IDENTIFIER",
    # Parenthesis
    "OPEN_PAR",
    "CLOSE_PAR",
    # Brace
    "OPEN_BRACE",
    "CLOSE_BRACE",
    # Semicolon
    "SEMICOLON",
]


class Parser:
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(ALPHABET)
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        #                                 p[0]    p[1]     p[2]
        @self.pg.production("wrapper : OPEN_BRACE block CLOSE_BRACE")
        def wrapper(p):
            return p[1]

        @self.pg.production("block : command")
        @self.pg.production("block : block command")
        def block(p):
            # initial block declaration
            if len(p) == 1:
                return Block(self.module, self.builder, None, [p[0]])
            # adds other commands to block
            p[0].children += [p[1]]
            return p[0]

        @self.pg.production("command : assignment SEMICOLON")
        @self.pg.production("command : print SEMICOLON")
        @self.pg.production("command : ifstmt")
        @self.pg.production("command : whilestmt")
        @self.pg.production("command : forstmt")
        @self.pg.production("command : wrapper")
        @self.pg.production("command : SEMICOLON")
        def command(p):
            # case SEMICOLON
            if isinstance(p[0], Token):
                return NoOp(None, None, None)
            return p[0]

        @self.pg.production("ifstmt : IF OPEN_PAR orexpr CLOSE_PAR command")
        @self.pg.production(
            "ifstmt : IF OPEN_PAR orexpr CLOSE_PAR command ELSE command"
        )
        def ifstmt(p):
            if len(p) == 5:
                return If(
                    self.module,
                    self.builder,
                    None,
                    [p[2], p[4], NoOp(None, None, None)],
                )
            elif len(p) == 7:
                return If(self.module, self.builder, None, [p[2], p[4], p[6]])
            else:
                raise ValueError("Should not reach this (ifstmt)")

        @self.pg.production("whilestmt : WHILE OPEN_PAR orexpr CLOSE_PAR command")
        def whilestmt(p):
            return While(self.module, self.builder, None, [p[2], p[4]])

        @self.pg.production(
            "forstmt : FOR OPEN_PAR assignment SEMICOLON orexpr SEMICOLON assignment CLOSE_PAR command"
        )
        def forstmt(p):
            return For(self.module, self.builder, None, [p[2], p[4], p[6], p[8]])

        @self.pg.production("assignment : VAR IDENTIFIER ASSIGN orexpr")
        @self.pg.production("assignment : IDENTIFIER ASSIGN orexpr")
        def assignment(p):
            if len(p) == 4:
                return Declare(self.module, self.builder, p[1].value, [p[3]])
            return Assign(self.module, self.builder, p[0].value, [p[2]])

        @self.pg.production("print : PRINT OPEN_PAR orexpr CLOSE_PAR")
        def print_prod(p):
            return Print(self.module, self.builder, None, [p[2]], self.printf)

        @self.pg.production("orexpr : andexpr")
        @self.pg.production("orexpr : orexpr OR andexpr")
        def orexrp(p):
            if len(p) == 1:
                return p[0]
            return LogicalOp(
                self.module, self.builder, p[1].gettokentype(), [p[0], p[2]]
            )

        @self.pg.production("andexpr : eqexpr")
        @self.pg.production("andexpr : andexpr AND eqexpr")
        def andexpr(p):
            if len(p) == 1:
                return p[0]
            return LogicalOp(
                self.module, self.builder, p[1].gettokentype(), [p[0], p[2]]
            )

        @self.pg.production("eqexpr : relexpr")
        @self.pg.production("eqexpr : eqexpr EQUAL relexpr")
        @self.pg.production("eqexpr : eqexpr NOT_EQUAL relexpr")
        def eqexpr(p):
            if len(p) == 1:
                return p[0]
            return LogicalOp(
                self.module, self.builder, p[1].gettokentype(), [p[0], p[2]]
            )

        @self.pg.production("relexpr : expression")
        @self.pg.production("relexpr : relexpr BIGGER expression")
        @self.pg.production("relexpr : relexpr BIGGER_EQ expression")
        @self.pg.production("relexpr : relexpr SMALLER expression")
        @self.pg.production("relexpr : relexpr SMALLER_EQ expression")
        def relexpr(p):
            if len(p) == 1:
                return p[0]
            return LogicalOp(
                self.module, self.builder, p[1].gettokentype(), [p[0], p[2]]
            )

        @self.pg.production("expression : expression PLUS term ")
        @self.pg.production("expression : expression MINUS term")
        @self.pg.production("expression : term")
        def expression(p):
            if len(p) == 1:
                return p[0]

            return BinOp(self.module, self.builder, p[1].gettokentype(), [p[0], p[2]])

        @self.pg.production("term : term MULT factor")
        @self.pg.production("term : term DIV factor")
        @self.pg.production("term : factor ")
        def term(p):
            if len(p) == 1:
                return p[0]
            return BinOp(self.module, self.builder, p[1].gettokentype(), [p[0], p[2]])

        @self.pg.production("factor : INTEGER")
        @self.pg.production("factor : IDENTIFIER")
        @self.pg.production("factor : NOT factor")
        @self.pg.production("factor : PLUS factor")
        @self.pg.production("factor : MINUS factor")
        @self.pg.production("factor : OPEN_PAR orexpr CLOSE_PAR")
        @self.pg.production("factor : READ OPEN_PAR CLOSE_PAR")
        def factor(p):
            if len(p) == 1:
                if p[0].gettokentype() == "INTEGER":
                    return IntVal(self.module, self.builder, int(p[0].value))
                elif p[0].gettokentype() == "IDENTIFIER":
                    return Identifier(self.module, self.builder, p[0].value)

            if len(p) == 2:
                return UnOp(self.module, self.builder, p[0].gettokentype(), [p[1]])

            elif len(p) == 3:
                if p[0].gettokentype() == "READ":
                    return Read(self.module, self.builder, None)
                return p[1]
            else:
                raise ValueError("Chegou onde não devia em factor")

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
