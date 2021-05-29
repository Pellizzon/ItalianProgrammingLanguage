# Programming Language in Italian

## EBNF
```

WRAPPER = FUNCDEF, { FUNCDEF } ;

FUNCDEF = "funzione", IDENTIFIER, "(", [ ARGUMENTS ], ")", BLOCK ;
ARGUMENTS = IDENTIFIER { ",", IDENTIFIER };

BLOCK = "{" { COMMAND } "}" ;
COMMAND = ( ASSIGNMENT | PRINT | FUNCTIONCALL | RETURN ), ";" | BLOCK | WHILESTMT | IFSMT | FUNCTIONDEF | FORSTMT ;

FUNCCALL = IDENTIFIER, "(", [ ORARGS ], ")" ;
ORARGS = OREXPR { ",", OREXPR };
RETURN = "ritorna", OREXPR ;  

FORSTMT = "per", "(", ASSIGNMENT, ";", OREXPR, ";", ASSIGNMENT, ")", COMMAND ;

ASSIGNMENT = ["var"], IDENTIFIER, "=", OREXPR ;
PRINT = "stampa", "(", OREXPR, ")" ;

IFSTMT = "se", "(", OREXPR, ")", COMMAND ["altro", COMMAND] ;
WHILESTMT = "mentre", "(", OREXPR, ")", COMMAND ;

OREXPR = ANDEXPR { "o", ANDEXPR } ;
ANDEXPR = BITOREXPR { "e", BITOREXPR } ;

BITOREXPR = BITXOREXPR { "|", BITXOREXPR } ;
BITXOREXPR = BITANDEXPR { "^", BITANDEXPR } ;
BITANDEXPR = EQEXPR { "&", EQEXPR } ;

EQEXPR = RELEXPR { ("==" | "!="), RELEXPR } ;
RELEXPR = SHIFTEXPR { (">" | "<" | "<=" | ">="), SHIFTEXPR } ;

SHIFTEXPR = EXPRESSION { ("<<" | ">>"), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = POWER, { ("*" | "/"), POWER } ;

POWER = FACTOR { "**", FACTOR } ;

FACTOR = (("+" | "-"| "non"), FACTOR) | NUMBER | "(", OREXPR, ")" | IDENTIFIER | READ | FUNCCALL ;
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

- C BNF example: https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm

- BASE/INSPIRATION: https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df

- RPLY MULTIPLE LINE LOGIC: https://stackoverflow.com/questions/60016733/how-to-parse-multiple-line-code-using-rply-library

- LLVMLITE DOCS: https://llvmlite.readthedocs.io/en/latest/user-guide/ir/ir-builder.html

- IF_ELSE: https://gist.github.com/sklam/eb89eab5b5708f03d0b971136a9806f4

- WHILE/FOR: https://github.com/symhom/Kaleidoscope_Compiler/blob/master/short_llvmlite_examples/while_loop_example.py

- SCANF: https://laratelli.com/posts/2020/06/generating-calls-to-scanf-from-llvm-ir/

- OPTMIZE (chapter3and4.py): https://github.com/eliben/pykaleidoscope 

- OPTMIZE: https://stackoverflow.com/questions/45171678/why-there-is-no-difference-when-i-change-the-level-of-optimizaition-in-llvmlite 
