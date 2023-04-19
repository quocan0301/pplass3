//2010829

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF ;

decl: vardecls | funcdecl;
vardecls: vardecl_init | vardecl | paradecl ;
vardecl: idlist COLON datatype SEMI;
idlist: ID COMMA idlist | ID;
vardecl_init: init SEMI;
init : ID COLON datatype EQ expr | ID COMMA init COMMA expr;
paradecl: INHER OUT ID COLON datatype | INHER ID COLON datatype | OUT ID COLON datatype | ID COLON datatype;
funcdecl: ID COLON FUNCT datatype LP paralist RP INHER ID block_statement| ID COLON FUNCT datatype LP paralist RP block_statement;
paralist: paralistt | ;
paralistt: paradecl  COMMA paralistt | paradecl ;

statement: if_statement
		| other;
other: block_statement
		| assign_statement
		| for_statement
		| while_statement
		| dowhile_statement
		| break_statement
		| continue_statement
		| return_statement
		| call_statement ;
block_statement: LB inner_block RB; 
inner_block: statement inner_block | vardecls inner_block | ;
assign_statement: initial SEMI;
if_statement: ifmatch | ifunmatch;
ifmatch: IF LP expr RP ifmatch ELSE ifmatch | other;
ifunmatch: IF LP expr RP if_statement | IF LP expr RP ifmatch ELSE ifunmatch;
for_statement: FOR LP initial COMMA expr COMMA expr RP statement;
initial: (ID | ID LS list_expr RS) EQ expr;
while_statement: WHILE LP expr RP statement;
dowhile_statement: DO block_statement WHILE LP expr RP SEMI; 
break_statement: BREAK SEMI;
continue_statement: CONT SEMI;
return_statement: RETURN expr SEMI | RETURN SEMI;
call_statement: ID LP list_expr RP SEMI;

COMMENT :  '/*' .*? '*/' -> skip;
LINE_COMMENT  : '//' ~[\r\n]* -> skip; 
WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines
fragment NUM: [0-9] NUM | [0-9];
fragment CHAR: ~[\b\f\r\n\t'"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt'"\\];
fragment ESC_ILL: '\\' ~[bfrnt'"\\] | '\\';

AUTO: 'auto';
BREAK: 'break';
BOOL: 'boolean';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
FUNCT: 'function';
IF: 'if';
INT: 'integer';
RETURN: 'return';
STR: 'string';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONT: 'continue';
OF: 'of';
INHER: 'inherit';
ARR: 'array';

ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NEQ: '!=';
SM: '<';
SMEQ: '<=';
BG: '>';
BGEQ: '>=';
STROP: '::';

LP: '('; RP: ')';
LB: '{'; RB: '}';
LS: '['; RS: ']';
EQ: '=';
COMMA: ',';
DOT: '.';
SEMI: ';';
COLON: ':';

ID: ([a-zA-Z]|'_') ([a-zA-Z0-9]|'_')*;
INTLIT: ([1-9] [0-9]* ('_'[0-9][0-9]*)* | '0') {self.text = self.text.replace('_','')};
FLOATLIT: (INTLIT DECPART | INTLIT DECPART EXPPART | INTLIT EXPPART) {self.text = self.text.replace('_','')};
DECPART: '.' NUM;
EXPPART: ('e' | 'E') '+' NUM | ('e' | 'E') '-' NUM | ('e' | 'E') NUM; 
BOOLIT: 'true' | 'false';
STRINGLIT: '"' CHAR* '"'  {self.text = self.text[1:-1]};

expr: expr1 STROP expr1 | expr1;
expr1: expr2 (EQUAL | NEQ | SM | SMEQ | BG | BGEQ) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD ) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: ID LS list_expr RS | expr8;
expr8: ID LP list_expr RP | expr9;
expr9: LP expr RP | ID | literal;
list_expr: expr_list | ;
expr_list: expr COMMA expr_list | expr;

literal: arrlit | INTLIT | FLOATLIT | BOOLIT | STRINGLIT;
arrlit: LB arraylist RB;
arraylist: array | ;
array: expr COMMA array| expr;
datatype: arrdecl | atomic | AUTO | VOID;
atomic: INT | FLOAT | BOOL | STR;
arrdecl: ARR LS dimension RS OF atomic;
dimension: di_list | ;
di_list: INTLIT COMMA di_list | INTLIT;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' CHAR* {raise UncloseString(self.text.replace('"','',1))};
ILLEGAL_ESCAPE: '"' CHAR* ESC_ILL {raise IllegalEscape(self.text.replace('"','',1))};