import sys
import warnings
from components.tokenizer import Lexer
from components.parser import Parser
from components.preprocessor import PreProcessor
from components.codeGen import CodeGen
from components.symbolTable import SymbolTable

if __name__ == "__main__":
    # suppress warnings
    warnings.simplefilter("ignore")

    with open(f"{sys.argv[1]}", "r") as f:
        inputData = f.read()

    # pre-process step, cleaning comments
    code = PreProcessor(inputData).filter()
    PreProcessor(code).check_PAR_balance()

    symbolTable = SymbolTable()

    # instantiate lexer object
    lexer = Lexer().get_lexer()
    # create tokens
    tokens = lexer.lex(code)

    # initialize llvmlite module, builder and buildInFunctions (pow, printf, sprinf)
    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    builtInFunctions = codegen.builtInFunctions

    # initialize parser
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    # parse tokens creating ast
    ast = parser.parse(tokens)
    # create llvm ir
    codegen.create_ir(ast, symbolTable)
    codegen.save_ir("output/output.ll")
