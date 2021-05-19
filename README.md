# JavaScript in Italiano (con alcuni adattamenti) EBNF

## EBNF
```
WRAPPER = { "{" block "}" }
BLOCK = command | block command ;
COMMAND = ( λ | ASSIGNMENT | PRINT | FUNCTIONCALL | RETURN), ";" ;
COMMAND =  BLOCK | WHILESTMT | IFSMT | FUNCTIONDEF | FORSTMT;

FUNCTIONDEF = "funzione", IDENTIFIER, "(", ARGUMENTS, ")", BLOCK ;
ARGUMENTS = [IDENTIFIER], {",", ARGUMENTS} ;
FUNCTIONCALL = IDENTIFIER, "(", [OREXPR], {",", OREXPR},")";
RETURN = "ritorna", [OREXPR];  

FORSTMT = "per", "(", ASSIGNMENT, ";", OREXPR, ";", ASSIGNMENT, ")", COMMAND ;

ASSIGNMENT = ["var"], IDENTIFIER, "=", OREXPR ;
PRINT = "stampa", "(", OREXPR, ")" ;
READ = "leggere", "(", ")";

IFSTMT = "se", "(", OREXPR, ")", COMMAND ["altro", COMMAND] ;
WHILESTMT = "mentre", "(", OREXPR, ")", COMMAND ;

OREXPR = ANDEXPR { "o", ANDEXPR } ;
ANDEXPR = EQEXPR { "e", EQEXPR } ;
EQEXPR = RELEXPR { ("==" | "!="), EQEXPR } ;
RELEXPR = EXPRESSION { (">" | "<" | "<=" | ">="), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"| "non"), FACTOR) | NUMBER | "(", OREXPR, ")" | IDENTIFIER | READ;
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

- https://joshsharp.com.au/blog/rpython-rply-interpreter-1.html

- https://stackoverflow.com/questions/60016733/how-to-parse-multiple-line-code-using-rply-library

- https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df

- https://llvmlite.readthedocs.io/en/latest/user-guide/ir/ir-builder.html

- https://gist.github.com/sklam/eb89eab5b5708f03d0b971136a9806f4

- https://github.com/symhom/Kaleidoscope_Compiler/blob/master/short_llvmlite_examples/while_loop_example.py

- https://github.com/rogerioag/llvm-gencode-samples

- https://laratelli.com/posts/2020/06/generating-calls-to-scanf-from-llvm-ir/
