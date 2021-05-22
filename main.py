import sys
import warnings
from components.tokenizer import Lexer
from components.parser import Parser
from components.preprocessor import PreProcessor
from components.codeGen import CodeGen
from components.symbolTable import SymbolTable

if __name__ == "__main__":
    # suppress warnings, such as "Token 'DEF_FUNC' is unused", since they're not implemented yet
    warnings.simplefilter("ignore")

    with open(f"{sys.argv[1]}", "r") as f:
        inputData = f.read()

    code = PreProcessor(inputData).filter()
    PreProcessor(code).check_PAR_balance()

    symbolTable = SymbolTable()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(code)

    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    builtInFunctions = codegen.builtInFunctions

    pg = Parser(module, builder, builtInFunctions)
    pg.parse()
    parser = pg.get_parser()

    ast = parser.parse(tokens)

    codegen.create_ir(ast, symbolTable)
    codegen.save_ir("output/output.ll")
