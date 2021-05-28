from components.symbolTable import SymbolTable
from llvmlite import ir


class Node:
    def __init__(self, initValue=None, initChildren=[]):
        self.value = initValue
        self.children = initChildren

    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        return


# Deals with binary operations,
# must have two children
class BinOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions, module
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
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions, module
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
            c1 = builder.icmp_signed(
                "!=", firstChildEval, ir.Constant(ir.IntType(32), 0)
            )
            c2 = builder.icmp_signed(
                "!=", secondChildEval, ir.Constant(ir.IntType(32), 0)
            )
            evaluate = builder.and_(c1, c2)
        elif self.value == "OR":
            c1 = builder.icmp_signed(
                "!=", firstChildEval, ir.Constant(ir.IntType(32), 0)
            )
            c2 = builder.icmp_signed(
                "!=", secondChildEval, ir.Constant(ir.IntType(32), 0)
            )
            evaluate = builder.or_(c1, c2)
        else:
            raise ValueError("Could not evaluate LogicalOp")

        return evaluate


class BitOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )

        if self.value == "XOR":
            evaluate = builder.xor(firstChildEval, secondChildEval)
        elif self.value == "BITWISE_AND":
            evaluate = builder.and_(firstChildEval, secondChildEval)
        elif self.value == "BITWISE_OR":
            evaluate = builder.or_(firstChildEval, secondChildEval)
        elif self.value == "LSHIFT":
            evaluate = builder.shl(firstChildEval, secondChildEval)
        elif self.value == "RSHIFT":
            evaluate = builder.lshr(firstChildEval, secondChildEval)
        else:
            raise ValueError("Could not evaluate LogicalOp")

        return evaluate


# Deals with unary operations,
# must have one child
class UnOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        childEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )

        if self.value == "PLUS":
            evaluate = childEval
        elif self.value == "MINUS":
            evaluate = builder.neg(childEval)
        elif self.value == "NOT":
            evaluate = builder.not_(childEval)
            evaluate = builder.add(evaluate, ir.Constant(ir.IntType(32), 1))
            evaluate = builder.icmp_signed(
                "!=", evaluate, ir.Constant(ir.IntType(32), 0)
            )
        else:
            raise ValueError("Could not evaluate UnOp")

        return evaluate


# Returns its own value, it's a "number" node
class IntVal(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        return ir.Constant(ir.IntType(32), int(self.value))


# no operation
class NoOp(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        return super().Evaluate(symbolTable, builder, builtInFunctions, module)


class Declare(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        varAddress = builder.alloca(ir.IntType(32), name=self.value)
        builder.store(
            self.children[0].Evaluate(symbolTable, builder, builtInFunctions, module),
            varAddress,
        )
        symbolTable.declare(self.value, varAddress)


# Assigns an identifier (received by self.value/initValue)
# to it's actual value (self.children[0].Evaluate(symbolTable, builder, builtInFunctions, module));
# Sets an Identfier's value on the Symbol Table
class Assign(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        varAddress = symbolTable.get(self.value)
        builder.store(
            self.children[0].Evaluate(symbolTable, builder, builtInFunctions, module),
            varAddress,
        )


# Contary to the Assign object, Identifier used to get
# an identifier's value from the Symbol Table
class Identifier(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        varAddress = symbolTable.get(self.value)
        return builder.load(varAddress)


class If(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        conditionalChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
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
                self.children[1].Evaluate(
                    symbolTable, builder, builtInFunctions, module
                )
            with orelse:
                # block or command child 2
                self.children[2].Evaluate(
                    symbolTable, builder, builtInFunctions, module
                )


class While(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        w_body_block = builder.append_basic_block("w_body")
        w_after_block = builder.append_basic_block("w_after")

        conditionalChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )

        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)

        # body
        builder.position_at_start(w_body_block)

        self.children[1].Evaluate(symbolTable, builder, builtInFunctions, module)

        conditionalChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)
        # after
        builder.position_at_start(w_after_block)


class For(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        self.children[0].Evaluate(symbolTable, builder, builtInFunctions, module)

        w_body_block = builder.append_basic_block("w_body")
        w_after_block = builder.append_basic_block("w_after")

        conditionalChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )

        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)

        # body
        builder.position_at_start(w_body_block)

        # code to execute
        self.children[3].Evaluate(symbolTable, builder, builtInFunctions, module)
        # increment of the declared variable
        self.children[2].Evaluate(symbolTable, builder, builtInFunctions, module)

        conditionalChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        conditionalChildEval = builder.icmp_signed(
            "!=", conditionalChildEval, ir.Constant(ir.IntType(32), 0)
        )
        builder.cbranch(conditionalChildEval, w_body_block, w_after_block)
        builder.position_at_start(w_after_block)


class Pow(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        firstChildEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        secondChildEval = self.children[1].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        power = builtInFunctions["pow"]
        return builder.call(power, [firstChildEval, secondChildEval])


# prints a value
# composed by identifiers and/or expressions
class Print(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        value = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )

        printf, printf_global_fmt, voidptr_ty = builtInFunctions["printf"]
        fmt_arg = builder.bitcast(printf_global_fmt, voidptr_ty)
        # Call Print Function
        builder.call(printf, [fmt_arg, value])


# receives an user input
# Value and Children are not needed
class Read(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        scanf, global_scanf_fmt, voidptr_ty = builtInFunctions["scanf"]
        fmt_arg = builder.bitcast(global_scanf_fmt, voidptr_ty)
        varAddress = builder.alloca(ir.IntType(32), name="temp")
        builder.call(scanf, [fmt_arg, varAddress])
        return builder.load(varAddress)


# A Block can have many instructions. Each line of code
# (instruction) is added as a child of block.
# When each child is evaluated, Assigns and Identifiers are
# being used to build the symbol table and eventualy
# Print a result
class Block(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        [
            i.Evaluate(symbolTable, builder, builtInFunctions, module)
            for i in self.children
        ]


class DeclareFunction(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        i32 = ir.IntType(32)
        if self.value != "main":
            if self.value in module.globals:
                raise ValueError(f"Cannot redeclare function '{self.value}'")
            args = [i32 for i in range(len(self.children[0]))]
            genericFunc_ty = ir.FunctionType(i32, args)
            generic_func = ir.Function(module, genericFunc_ty, name=self.value)
            block = generic_func.append_basic_block("entry")
            builder = ir.IRBuilder(block)

            for i in range(len(generic_func.args)):
                address = builder.alloca(i32, name=self.children[0][i])
                builder.store(generic_func.args[i], address)
                symbolTable.declare(self.children[0][i], address)

            self.children[1].Evaluate(symbolTable, builder, builtInFunctions, module)
            if not symbolTable.contains("return"):
                # functions with no return always return 0
                builder.ret(ir.Constant(i32, 0))
            else:
                symbolTable.dropReturn()
            return generic_func
        else:
            self.children[1].Evaluate(symbolTable, builder, builtInFunctions, module)
            return


class Return(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        childEval = self.children[0].Evaluate(
            symbolTable, builder, builtInFunctions, module
        )
        symbolTable.declare("return", childEval)
        return builder.ret(childEval)


class FunctionCall(Node):
    def Evaluate(self, symbolTable, builder, builtInFunctions, module):
        if self.value not in module.globals:
            raise ValueError(f"tried to call inexistent function '{self.value}'")

        fun = module.globals[self.value]
        funcArgs = fun.args
        if len(funcArgs) != len(self.children):
            raise ValueError("Number of arguments mismatch")

        args = []
        for i in range(len(funcArgs)):
            childEval = self.children[i].Evaluate(
                symbolTable, builder, builtInFunctions, module
            )
            args += [childEval]

        return builder.call(fun, args)