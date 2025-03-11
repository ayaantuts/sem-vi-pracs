/*** Definition section ***/
/*** find keywords of C ***/
%option noyywrap
%{
	
%}

%%
"auto" { printf("Keyword found: auto\n"); }
"break" { printf("Keyword found: break\n"); }
"case" { printf("Keyword found: case\n"); }
"char" { printf("Keyword found: char\n"); }
"const" { printf("Keyword found: const\n"); }
"continue" { printf("Keyword found: continue\n"); }
"default" { printf("Keyword found: default\n"); }
"do" { printf("Keyword found: do\n"); }
"double" { printf("Keyword found: double\n"); }
"else" { printf("Keyword found: else\n"); }
"enum" { printf("Keyword found: enum\n"); }
"extern" { printf("Keyword found: extern\n"); }
"float" { printf("Keyword found: float\n"); }
"for" { printf("Keyword found: for\n"); }
"goto" { printf("Keyword found: goto\n"); }
"if" { printf("Keyword found: if\n"); }
"int" { printf("Keyword found: int\n"); }
"long" { printf("Keyword found: long\n"); }
"register" { printf("Keyword found: register\n"); }
"return" { printf("Keyword found: return\n"); }
"short" { printf("Keyword found: short\n"); }
"signed" { printf("Keyword found: signed\n"); }
"sizeof" { printf("Keyword found: sizeof\n"); }
"static" { printf("Keyword found: static\n"); }
"struct" { printf("Keyword found: struct\n"); }
"switch" { printf("Keyword found: switch\n"); }
"typedef" { printf("Keyword found: typedef\n"); }
"union" { printf("Keyword found: union\n"); }
"unsigned" { printf("Keyword found: unsigned\n"); }
"void" { printf("Keyword found: void\n"); }
"volatile" { printf("Keyword found: volatile\n"); }
"while" { printf("Keyword found: while\n"); }
. { /* ignore other characters */ }
\n { return 0; }
%%

/*** C Code section ***/
int main(void)
{
	yylex();
	return 0;
}