import sys
from components.tokenizer import Lexer
from components.parser import Parser
from components.preprocessor import PreProcessor
from components.codeGen import CodeGen
from components.node import symbolTable

if __name__ == "__main__":

    if not sys.argv[1].endswith(".c"):
        raise ValueError("Input file must have '.c' extension")

    with open(f"{sys.argv[1]}", "r") as f:
        inputData = f.read()

    code = PreProcessor(inputData).filter()
    PreProcessor(code).check_PAR_balance()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(code)

    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf

    pg = Parser(module, builder, printf)
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).Evaluate()

    codegen.create_ir()
    codegen.save_ir("output/output.ll")
