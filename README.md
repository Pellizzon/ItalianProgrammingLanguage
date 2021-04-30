# JavaScript in Italiano (con alcuni adattamenti) EBNF

EBNF
```
BLOCK = { "{", COMMAND, "}" } ;
COMMAND = ( λ | ASSIGNMENT | PRINT | READ | FUNCTIONCALL | RETURN), ";" | BLOCK | WHILESTMT | IFSMT | FUNCTIONDEF | FORSTMT;

FUNCTIONDEF = "funzione", IDENTIFIER, "(", ARGUMENTS, ")", BLOCK ;
ARGUMENTS = [IDENTIFIER], {",", ARGUMENTS} ;
FUNCTIONCALL = IDENTIFIER, "(", [OREXPR], {",", OREXPR},")";
RETURN = "ritorna", [OREXPR]; 

FORSTMT = "per", "(", ASSIGNMENT, ";", OREXPR, ";", EXPRESSION, ")", COMMAND ;

ASSIGNMENT = IDENTIFIER, "=", OREXPR ;
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
