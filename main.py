import sys
from components.parser import Parser

if __name__ == "__main__":

    if not sys.argv[1].endswith(".c"):
        raise ValueError("Input file must have '.c' extension")

    with open(f"{sys.argv[1]}", "r") as f:
        inputData = f.read()

    Parser().run(inputData).Evaluate()
