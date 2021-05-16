from components.symbolTable import SymbolTable
from llvmlite import ir

symbolTable = SymbolTable()


class Node:
    def __init__(self, module, builder, initValue, initChildren=[], printf=None):
        self.module = module
        self.builder = builder
        self.value = initValue
        self.children = initChildren
        self.printf = printf

    def Evaluate(self):
        return


# Deals with binary operations,
# must have two children
class BinOp(Node):
    def Evaluate(self):
        firstChildEval = self.children[0].Evaluate()
        secondChildEval = self.children[1].Evaluate()

        if self.value == "PLUS":
            evaluate = self.builder.add(firstChildEval, secondChildEval)
        elif self.value == "MINUS":
            evaluate = self.builder.sub(firstChildEval, secondChildEval)
        elif self.value == "DIV":
            evaluate = self.builder.sdiv(firstChildEval, secondChildEval)
        elif self.value == "MULT":
            evaluate = self.builder.mul(firstChildEval, secondChildEval)
        else:
            raise ValueError("Could not evaluate BinOp")

        return evaluate


# Deals with Logical operations,
# must have two children
class LogicalOp(Node):
    def Evaluate(self):
        firstChildEval = self.children[0].Evaluate()
        secondChildEval = self.children[1].Evaluate()

        if self.value == "SMALLER":
            evaluate = self.builder.icmp_signed("<", firstChildEval, secondChildEval)
        elif self.value == "BIGGER":
            evaluate = self.builder.icmp_signed(">", firstChildEval, secondChildEval)
        elif self.value == "SMALLER_EQ":
            evaluate = self.builder.icmp_signed("<=", firstChildEval, secondChildEval)
        elif self.value == "BIGGER_EQ":
            evaluate = self.builder.icmp_signed(">=", firstChildEval, secondChildEval)
        elif self.value == "NOT_EQUAL":
            evaluate = self.builder.icmp_signed("!=", firstChildEval, secondChildEval)
        elif self.value == "EQUAL":
            evaluate = self.builder.icmp_signed("==", firstChildEval, secondChildEval)
        elif self.value == "AND":
            evaluate = self.builder.and_(firstChildEval, secondChildEval)
        elif self.value == "OR":
            evaluate = self.builder.or_(firstChildEval, secondChildEval)
        else:
            raise ValueError("Could not evaluate LogicalOp")

        return evaluate


# Deals with unary operations,
# must have one child
class UnOp(Node):
    def Evaluate(self):
        childEval = self.children[0].Evaluate()

        if self.value == "PLUS":
            evaluate = childEval
        elif self.value == "MINUS":
            evaluate = self.builder.neg(childEval)
        elif self.value == "NOT":
            # builder.not_ returns Bitwise complement value, which is not what is expected in my language
            # evaluate = self.builder.not_(childEval)
            childEval.constant = 1 if childEval.constant == 0 else 0
            evaluate = childEval
        else:
            raise ValueError("Could not evaluate UnOp")

        return evaluate


# Returns its own value, it's a "number" node
class IntVal(Node):
    def Evaluate(self):
        return ir.Constant(ir.IntType(32), int(self.value))


# no operation
class NoOp(Node):
    def Evaluate(self):
        return super().Evaluate()


class Declare(Node):
    def Evaluate(self):
        varAddress = self.builder.alloca(ir.IntType(32), name=self.value)
        self.builder.store(self.children[0].Evaluate(), varAddress)
        symbolTable.declare(self.value, varAddress)


# Assigns an identifier (received by self.value/initValue)
# to it's actual value (self.children[0].Evaluate());
# Sets an Identfier's value on the Symbol Table
class Assign(Node):
    def Evaluate(self):
        varAddress = symbolTable.get(self.value)
        self.builder.store(self.children[0].Evaluate(), varAddress)


# Contary to the Assign object, Identifier used to get
# an identifier's value from the Symbol Table
class Identifier(Node):
    def Evaluate(self):
        varAddress = symbolTable.get(self.value)
        return self.builder.load(varAddress)


class If(Node):
    def Evaluate(self):
        conditionalChildEval = self.children[0].Evaluate()
        # if_else must receive an icmp obj.
        # cases like:
        # if (x) or if(3)
        # wont work, so we must have a workaround
        conditionalChildEval = self.builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        with self.builder.if_else(conditionalChildEval) as (then, orelse):
            with then:
                # block or command child 1
                self.children[1].Evaluate()
            with orelse:
                # block or command child 2
                self.children[2].Evaluate()


class While(Node):
    def Evaluate(self):
        w_body_block = self.builder.append_basic_block("w_body")
        w_after_block = self.builder.append_basic_block("w_after")

        conditionalChildEval = self.children[0].Evaluate()
        conditionalChildEval = self.builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )

        self.builder.cbranch(conditionalChildEval, w_body_block, w_after_block)

        # body
        self.builder.position_at_start(w_body_block)

        self.children[1].Evaluate()

        conditionalChildEval = self.children[0].Evaluate()
        conditionalChildEval = self.builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        self.builder.cbranch(conditionalChildEval, w_body_block, w_after_block)
        # after
        self.builder.position_at_start(w_after_block)


class For(Node):
    def Evaluate(self):
        self.children[0].Evaluate()

        w_body_block = self.builder.append_basic_block("w_body")
        w_after_block = self.builder.append_basic_block("w_after")

        conditionalChildEval = self.children[1].Evaluate()
        conditionalChildEval = self.builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )

        self.builder.cbranch(conditionalChildEval, w_body_block, w_after_block)

        # body
        self.builder.position_at_start(w_body_block)

        # code to execute
        self.children[3].Evaluate()
        # increment of the declared variable
        self.children[2].Evaluate()

        conditionalChildEval = self.children[1].Evaluate()
        conditionalChildEval = self.builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        self.builder.cbranch(conditionalChildEval, w_body_block, w_after_block)
        self.builder.position_at_start(w_after_block)


# prints a value
# composed by identifiers and/or expressions
class Print(Node):
    def Evaluate(self):
        value = self.children[0].Evaluate()

        printf, fmt_arg = self.printf

        # Call Print Function
        self.builder.call(printf, [fmt_arg, value])


# receives an user input
# Value and Children are not needed
class Read(Node):
    def Evaluate(self):
        return ir.Constant(ir.IntType(32), int(input()))


# A Block can have many instructions. Each line of code
# (instruction) is added as a child of block.
# When each child is evaluated, Assigns and Identifiers are
# being used to build the symbol table and eventualy
# Print a result
class Block(Node):
    def Evaluate(self):
        [i.Evaluate() for i in self.children]
