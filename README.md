# JavaScript in Italiano (con alcuni adattamenti) EBNF

## EBNF
```
WRAPPER = "{" BLOCK "}"
BLOCK = COMMAND | BLOCK COMMAND ;
COMMAND = ( λ | ASSIGNMENT | PRINT | FUNCTIONCALL | RETURN), ";" ;
COMMAND =  BLOCK | WHILESTMT | IFSMT | FUNCTIONDEF | FORSTMT;

FUNCTIONDEF = "funzione", IDENTIFIER, "(", ARGUMENTS, ")", BLOCK ;
ARGUMENTS = [IDENTIFIER], {",", ARGUMENTS} ;
FUNCTIONCALL = IDENTIFIER, "(", [OREXPR], {",", OREXPR},")";
RETURN = "ritorna", [OREXPR];  

FORSTMT = "per", "(", ASSIGNMENT, ";", OREXPR, ";", ASSIGNMENT, ")", COMMAND ;

ASSIGNMENT = ["var"], IDENTIFIER, "=", OREXPR ;
PRINT = "stampa", "(", OREXPR, ")" ;

IFSTMT = "se", "(", OREXPR, ")", COMMAND ["altro", COMMAND] ;
WHILESTMT = "mentre", "(", OREXPR, ")", COMMAND ;

OREXPR = ANDEXPR { "o", OREXPR } ;
ANDEXPR = EQEXPR { "e", ANDEXPR } ;
EQEXPR = RELEXPR { ("==" | "!="), EQEXPR } ;
RELEXPR = BITEXPR { (">" | "<" | "<=" | ">="), RELEXPR } ;

BITEXPR = EXPRESSION { ("|" | "&" | "^"), BITEXPR } 

EXPRESSION = TERM, { ("+" | "-"), EXPRESSION } ;
TERM = POWER, { ("*" | "/"), TERM } ;

POWER = FACTOR { "**", POWER }

FACTOR = (("+" | "-"| "non"), FACTOR) | NUMBER | "(", OREXPR, ")" | IDENTIFIER | READ;
READ = "leggere", "(", ")";
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```

## Requirements

### llvmlite:

```conda install --channel=numba llvmlite``` or ```pip install numba```

### rply

```conda install -c conda-forge rply``` or ```pip install rply```

## Running a program:
```./run.sh <file>```

References:

- BASE/INSPIRATION: https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df

- RPLY MULTIPLE LINE LOGIC: https://stackoverflow.com/questions/60016733/how-to-parse-multiple-line-code-using-rply-library

- LLVMLITE DOCS: https://llvmlite.readthedocs.io/en/latest/user-guide/ir/ir-builder.html

- IF_ELSE: https://gist.github.com/sklam/eb89eab5b5708f03d0b971136a9806f4

- WHILE/FOR: https://github.com/symhom/Kaleidoscope_Compiler/blob/master/short_llvmlite_examples/while_loop_example.py

- SCANF: https://laratelli.com/posts/2020/06/generating-calls-to-scanf-from-llvm-ir/

- OPTMIZE (chapter3and4.py): https://github.com/eliben/pykaleidoscope
