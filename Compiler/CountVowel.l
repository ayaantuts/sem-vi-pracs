/*** Definition section ***/
%option noyywrap
%{
	int vowelCount = 0;
%}

%%
[aeiouAEIOU] { vowelCount++; }
. { /* ignore other characters */ }
\n { printf("Number of vowels: %d\n", vowelCount); return 0; }
%%

/*** C Code section ***/
int main(void)
{
	yylex();
	return 0;
}