/*** Definition section ***/
/*** count number of words ***/
%option noyywrap
%{
	int count = 0;
%}

%%
[ \t]+ { /* ignore white space */ }
[a-zA-Z]+ { count++; }
. { /* ignore other characters */ }
\n { printf("Number of words: %d\n", count); return 0; }
%%

/*** C Code section ***/
int main(void)
{
	yylex();
	return 0;
}