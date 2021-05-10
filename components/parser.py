from components.preprocessor import PrePro
from components.token import Token
from components.tokenizer import Tokenizer
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
)
from components.symbolTable import SymbolTable


class Parser:
    def __init__(self):
        self.tokens = None

    def parseFactor(self):
        self.tokens.nextToken()
        if self.tokens.actual.type == "INT":
            return IntVal(self.tokens.actual.value)
        elif self.tokens.actual.type in ["PLUS", "MINUS", "NOT"]:
            return UnOp(self.tokens.actual.type, [self.parseFactor()])
        elif self.tokens.actual.type == "LPAR":
            exp = self.parseOrExpr()
            if self.tokens.actual.type == "RPAR":
                return exp
            else:
                raise ValueError("Could not close parenthesis")
        elif self.tokens.actual.type == "IDENTIFIER":
            return Identifier(self.tokens.actual.value)
        elif self.tokens.actual.type == "READ":
            self.tokens.nextToken()
            if self.tokens.actual.value != "(":
                raise ValueError("readln must be followed by (")
            self.tokens.nextToken()
            if self.tokens.actual.value != ")":
                raise ValueError("readln( must be followed by )")
            return Read(None)
        else:
            raise ValueError("Cannot parse Factor")

    def parseTerm(self):
        resultado = self.parseFactor()
        self.tokens.nextToken()
        while self.tokens.actual.type in ["MULT", "DIV"]:
            if self.tokens.actual.type in ["MULT", "DIV"]:
                resultado = BinOp(
                    self.tokens.actual.type, [resultado, self.parseFactor()]
                )
            else:
                raise ValueError("Could not complete parseTerm")
            self.tokens.nextToken()
        return resultado

    def parseExpression(self):
        result = self.parseTerm()
        while self.tokens.actual.type in ["PLUS", "MINUS"]:
            if self.tokens.actual.type in ["PLUS", "MINUS"]:
                result = BinOp(self.tokens.actual.type, [result, self.parseTerm()])
            else:
                raise ValueError("Error: it never should reach this")
        return result

    def parseRelExpr(self):
        result = self.parseExpression()
        while self.tokens.actual.type in ["LESSTHAN", "BIGGERTHAN"]:
            if self.tokens.actual.type in ["LESSTHAN", "BIGGERTHAN"]:
                result = LogicalOp(
                    self.tokens.actual.type, [result, self.parseExpression()]
                )
            else:
                raise ValueError("Error: it never should reach this")
        return result

    def parseEqExpr(self):
        result = self.parseRelExpr()
        while self.tokens.actual.type in ["EQOP"]:
            if self.tokens.actual.type in ["EQOP"]:
                result = LogicalOp(
                    self.tokens.actual.type, [result, self.parseRelExpr()]
                )
            else:
                raise ValueError("Error: it never should reach this")
        return result

    def parseAndExpr(self):
        result = self.parseEqExpr()
        while self.tokens.actual.type in ["AND"]:
            if self.tokens.actual.type in ["AND"]:
                result = LogicalOp(
                    self.tokens.actual.type, [result, self.parseEqExpr()]
                )
            else:
                raise ValueError("Error: it never should reach this")
        return result

    def parseOrExpr(self):
        result = self.parseAndExpr()
        while self.tokens.actual.type in ["OR"]:
            if self.tokens.actual.type in ["OR"]:
                result = LogicalOp(
                    self.tokens.actual.type, [result, self.parseAndExpr()]
                )
            else:
                raise ValueError("Error: it never should reach this")
        return result

    def parseCommand(self):
        if self.tokens.actual.type == "IDENTIFIER":
            identifier = self.tokens.actual.value
            self.tokens.nextToken()
            if self.tokens.actual.type != "EQUAL":
                raise ValueError(
                    f"Variable assignments must be followed by '=', but got '{self.tokens.actual.value}'"
                )
            result = Assign(identifier, [self.parseOrExpr()])

            if (self.tokens.actual.value) != ";":
                raise ValueError(
                    f"Commands must end with ';', but got '{self.tokens.actual.value}'"
                )
            self.tokens.nextToken()

        elif self.tokens.actual.type == "PRINT":
            self.tokens.nextToken()
            if self.tokens.actual.type != "LPAR":
                raise ValueError(
                    f"println must be followed by '(', got '{self.tokens.actual.value}'"
                )
            result = Print(None, [self.parseOrExpr()])
            if self.tokens.actual.type != "RPAR":
                raise ValueError(
                    f"println must end with ')', got '{self.tokens.actual.value}'"
                )
            self.tokens.nextToken()

            if (self.tokens.actual.value) != ";":
                raise ValueError(
                    f"Commands must end with ';', but got '{self.tokens.actual.value}'"
                )

            self.tokens.nextToken()

        elif self.tokens.actual.type == "WHILE":
            self.tokens.nextToken()
            if self.tokens.actual.type != "LPAR":
                raise ValueError(
                    f"println must be followed by '(', got '{self.tokens.actual.value}'"
                )
            orExpr = self.parseOrExpr()
            if self.tokens.actual.type != "RPAR":
                raise ValueError(
                    f"println must end with ')', got '{self.tokens.actual.value}'"
                )
            self.tokens.nextToken()
            result = While(None, [orExpr, self.parseCommand()])

        elif self.tokens.actual.type == "IF":
            self.tokens.nextToken()
            if self.tokens.actual.type != "LPAR":
                raise ValueError(
                    f"println must be followed by '(', got '{self.tokens.actual.value}'"
                )
            orExpr = self.parseOrExpr()
            if self.tokens.actual.type != "RPAR":
                raise ValueError(
                    f"println must end with ')', got '{self.tokens.actual.value}'"
                )
            self.tokens.nextToken()
            trueBlock = self.parseCommand()
            result = If(None, [orExpr, trueBlock])

            if self.tokens.actual.type == "ELSE":
                self.tokens.nextToken()
                falseBlock = self.parseCommand()
                result = If(None, [orExpr, trueBlock, falseBlock])
            else:
                pass

        elif self.tokens.actual.value == "{":
            result = self.parseBlock()
            self.tokens.nextToken()

        else:
            result = NoOp(None)
            # cases like +1+2*2; enter here
            # they would raise errors on the next if ";".
            # just to manage errors more precisely, some will be treated here
            if (str(self.tokens.actual.value) in "()+-*/=") or (
                self.tokens.actual.type == "INT"
            ):
                raise ValueError(
                    "Commands must be Assignments or Prints, Ifs or Whiles"
                )

            if (self.tokens.actual.value) != ";":
                raise ValueError(
                    f"Commands must end with ';', but got '{self.tokens.actual.value}'"
                )
            self.tokens.nextToken()

        return result

    def parseBlock(self):
        if self.tokens.actual.value != "{":
            raise ValueError("Block must start with '{'")
        executedCommands = []
        self.tokens.nextToken()
        while self.tokens.actual.value != "}":
            executedCommands += [self.parseCommand()]

        return Block(None, executedCommands)

    def run(self, code):
        code = PrePro(code).filter()
        PrePro(code).check_PAR_balance()
        self.tokens = Tokenizer(code)
        self.tokens.tokenize()

        self.tokens.nextToken()
        result = self.parseBlock()
        self.tokens.nextToken()

        if self.tokens.actual.type != "EOF":
            raise ValueError("Did not reach EOF")
        return result