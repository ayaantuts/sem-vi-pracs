// Implement Lexical Analysis using C (print symbol table)
/* Re-write */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isKeyword(char buffer[]) {
	char keywords[32][10] = {
		"auto", "break", "case", "char", "const", "continue", "default",
		"do", "double", "else", "enum", "extern", "float", "for", "goto",
		"if", "int", "long", "register", "return", "short", "signed",
		"sizeof", "static", "struct", "switch", "typedef", "union",
		"unsigned", "void", "volatile", "while"
	};
	int i, flag = 0;
	for (i = 0; i < 32; ++i) {
		if (strcmp(keywords[i], buffer) == 0) {
			flag = 1;
			break;
		}
	}
	return flag;
}

int isOperator(char ch) {
	char operators[] = "+-*/%=";
	int i, flag = 0;
	for (i = 0; i < 6; ++i) {
		if (ch == operators[i]) {
			flag = 1;
			break;
		}
	}
	return flag;
}

int isDelimiter(char ch) {
	char delimiters[] = " ,;{}()";
	int i, flag = 0;
	for (i = 0; i < 6; ++i) {
		if (ch == delimiters[i]) {
			flag = 1;
			break;
		}
	}
	return flag;
}

int isString(char *buffer) {
	int i, flag = 0;
	if (buffer[0] == '"' || buffer[0] == '\'') {
		flag = 1;
	} for (i = 1; i < strlen(buffer); i++) {
		if (buffer[i] == buffer[0] || buffer[i] == buffer[0]) {
			flag = 1;
			break;
		}
	}
	return flag;
}

int main() {
	char ch, buffer[15], operators[] = "+-*/%=", strSeparator;
	FILE *fp;
	int i, j = 0;
	fp = fopen("lex.txt", "r");
	if (fp == NULL) {
		printf("error while opening the file\n");
		return 0;
	} else {
		printf("file opened successfully\n");
	}
	while ((ch = fgetc(fp)) != EOF) {
		if (isDelimiter(ch) == 1) {
			if (strSeparator && (ch == ' ' || ch == '\n')) {
				buffer[j++] = ch;
			} else if (ch == ' ' || ch == '\n')
				continue;
			else
				printf("%c is delimiter\n", ch);
		} else if (isOperator(ch) == 1) {
			printf("%c is operator\n", ch);
		} else {
			if (isalnum(ch)) {
				buffer[j++] = ch;
			} else if ((ch == ' ' || ch == '\n') && (j != 0)) {
				buffer[j] = '\0';
				j = 0;
				if (isKeyword(buffer) == 1) {
					printf("%s is keyword\n", buffer);
				} else {
					if (isString(buffer) == 1) {
						printf("%s is string\n", buffer);
					} else {
						printf("%s is identifier\n", buffer);
					}
				}
			}
		}
		printf("%s\n", buffer);
	}
	fclose(fp);
	return 0;
}