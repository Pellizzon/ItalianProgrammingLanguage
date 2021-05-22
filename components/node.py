from components.symbolTable import SymbolTable
from llvmlite import ir


class Node:
    def __init__(self, initValue=None, initChildren=[]):
        self.value = initValue
        self.children = initChildren

    def Evaluate(self, symbolTable, builder, builtInFunctions):
        return


# Deals with binary operations,
# must have two children
class BinOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions
        )

        if self.value == "PLUS":
            evaluate = builder.add(firstChildEval, secondChildEval)
        elif self.value == "MINUS":
            evaluate = builder.sub(firstChildEval, secondChildEval)
        elif self.value == "DIV":
            evaluate = builder.sdiv(firstChildEval, secondChildEval)
        elif self.value == "DIV_REST":
            evaluate = builder.srem(firstChildEval, secondChildEval)
        elif self.value == "MULT":
            evaluate = builder.mul(firstChildEval, secondChildEval)
        else:
            raise ValueError("Could not evaluate BinOp")

        return evaluate


# Deals with Logical operations,
# must have two children
class LogicalOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions
        )

        if self.value == "SMALLER":
            evaluate = builder.icmp_signed("<", firstChildEval, secondChildEval)
        elif self.value == "BIGGER":
            evaluate = builder.icmp_signed(">", firstChildEval, secondChildEval)
        elif self.value == "SMALLER_EQ":
            evaluate = builder.icmp_signed("<=", firstChildEval, secondChildEval)
        elif self.value == "BIGGER_EQ":
            evaluate = builder.icmp_signed(">=", firstChildEval, secondChildEval)
        elif self.value == "NOT_EQUAL":
            evaluate = builder.icmp_signed("!=", firstChildEval, secondChildEval)
        elif self.value == "EQUAL":
            evaluate = builder.icmp_signed("==", firstChildEval, secondChildEval)
        elif self.value == "AND":
            evaluate = builder.and_(firstChildEval, secondChildEval)
        elif self.value == "OR":
            evaluate = builder.or_(firstChildEval, secondChildEval)
        else:
            raise ValueError("Could not evaluate LogicalOp")

        return evaluate


class BitOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions
        )

        if self.value == "XOR":
            evaluate = builder.xor(firstChildEval, secondChildEval)
        elif self.value == "BITWISE_AND":
            evaluate = builder.and_(firstChildEval, secondChildEval)
        elif self.value == "BITWISE_OR":
            evaluate = builder.or_(firstChildEval, secondChildEval)
        else:
            raise ValueError("Could not evaluate LogicalOp")

        return evaluate


# Deals with unary operations,
# must have one child
class UnOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        childEval = self.children[0].Evaluate(symbolTable, builder, builtInFunctions)

        if self.value == "PLUS":
            evaluate = childEval
        elif self.value == "MINUS":
            evaluate = builder.neg(childEval)
        elif self.value == "NOT":
            # builder.not_ returns Bitwise complement value, which is not what is expected in my language
            # evaluate = builder.not_(childEval)
            childEval.constant = 1 if childEval.constant == 0 else 0
            evaluate = childEval
        else:
            raise ValueError("Could not evaluate UnOp")

        return evaluate


# Returns its own value, it's a "number" node
class IntVal(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        return ir.Constant(ir.IntType(32), int(self.value))


# no operation
class NoOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        return super().Evaluate(symbolTable, builder, builtInFunctions)


class Declare(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        varAddress = builder.alloca(ir.IntType(32), name=self.value)
        builder.store(
            self.children[0].Evaluate(symbolTable, builder, builtInFunctions),
            varAddress,
        )
        symbolTable.declare(self.value, varAddress)


# Assigns an identifier (received by self.value/initValue)
# to it's actual value (self.children[0].Evaluate(symbolTable, builder, builtInFunctions));
# Sets an Identfier's value on the Symbol Table
class Assign(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        varAddress = symbolTable.get(self.value)
        builder.store(
            self.children[0].Evaluate(symbolTable, builder, builtInFunctions),
            varAddress,
        )


# Contary to the Assign object, Identifier used to get
# an identifier's value from the Symbol Table
class Identifier(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        varAddress = symbolTable.get(self.value)
        return builder.load(varAddress)


class If(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        conditionalChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        # if_else must receive an icmp obj.
        # cases like:
        # if (x) or if(3)
        # wont work, so we must have a workaround
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        with builder.if_else(conditionalChildEval) as (then, orelse):
            with then:
                # block or command child 1
                self.children[1].Evaluate(symbolTable, builder, builtInFunctions)
            with orelse:
                # block or command child 2
                self.children[2].Evaluate(symbolTable, builder, builtInFunctions)


class While(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        w_body_block = builder.append_basic_block("w_body")
        w_after_block = builder.append_basic_block("w_after")

        conditionalChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )

        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)

        # body
        builder.position_at_start(w_body_block)

        self.children[1].Evaluate(symbolTable, builder, builtInFunctions)

        conditionalChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)
        # after
        builder.position_at_start(w_after_block)


class For(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        self.children[0].Evaluate(symbolTable, builder, builtInFunctions)

        w_body_block = builder.append_basic_block("w_body")
        w_after_block = builder.append_basic_block("w_after")

        conditionalChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )

        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)

        # body
        builder.position_at_start(w_body_block)

        # code to execute
        self.children[3].Evaluate(symbolTable, builder, builtInFunctions)
        # increment of the declared variable
        self.children[2].Evaluate(symbolTable, builder, builtInFunctions)

        conditionalChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)
        builder.position_at_start(w_after_block)


class Pow(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions
        )
        power = builtInFunctions["pow"]
        return builder.call(power, [firstChildEval, secondChildEval])


# prints a value
# composed by identifiers and/or expressions
class Print(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        value = self.children[0].Evaluate(symbolTable, builder, builtInFunctions)

        printf, fmt_arg = builtInFunctions["printf"]

        # Call Print Function
        builder.call(printf, [fmt_arg, value])


# receives an user input
# Value and Children are not needed
class Read(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        scanf, fmt_arg = builtInFunctions["scanf"]
        varAddress = builder.alloca(ir.IntType(32), name="temp")
        builder.call(scanf, [fmt_arg, varAddress])
        return builder.load(varAddress)


# A Block can have many instructions. Each line of code
# (instruction) is added as a child of block.
# When each child is evaluated, Assigns and Identifiers are
# being used to build the symbol table and eventualy
# Print a result
class Block(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions):
        [i.Evaluate(symbolTable, builder, builtInFunctions) for i in self.children]
