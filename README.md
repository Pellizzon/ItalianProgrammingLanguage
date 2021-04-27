# APSLogica

EBNF

```
BLOCK = { "{", COMMAND, "}" } ;
COMMAND = (( λ | ASSIGNMENT | PRINT | RETURN), ";" | (LOOPSTMT | IFSTMT | FUNCTIONSTMT)) ;
LOOPSTMT = "mentre", CONDITION_EXP, BLOCK;
IFSTMT = "se", CONDITION_EXP, BLOCK, ["altro", BLOCK] ;
CONDITION_EXP = "(", CONDITION, {LOGICALOP, CONDITION}, ")" ;  
CONDITION = EXPRESSION, LOGICALOP, EXPRESSION | "non", EXPRESSION ;
FUNCTIONDEF = "funzione", IDENTIFIER, "(", ARGUMENTS, ")", BLOCK ;
ARGUMENTS = [IDENTIFIER], {",", ARGUMENTS} ;
FUNCTIONCALL = IDENTIFIER, "(", [EXPRESSION], {",", EXPRESSION},")";
RETURN = "ritorna", [EXPRESSION]; 
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
PRINT = "stampa", "(", EXPRESSION, ")" ;
EXPRESSION = (UNOP, (NUMBER | IDENTIFIER)) | ((NUMBER | IDENTIFIER) BINOP (NUMBER | IDENTIFIER)) ; 
UNOP = ("+" | "-") ;
LOGICALOP = ("e" | "o" | ">" | ">=" | "<" | "<=" | "!=" | "==") ;
BOOLEAN = ("vero" | "falso") ; 
BINOP = (UNOP | LOGICALOP | "*" | "/" | "%") ; 
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```
