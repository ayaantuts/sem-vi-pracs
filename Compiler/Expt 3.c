#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// Define MAX size for the grammar components
#define MAX 10

// Declare arrays to hold terminals, non-terminals, and productions
char terminals[MAX], nonterminals[MAX], **productions;
int n, t, nt;

// Node structure for the linked list to store sets
struct Node {
    char symbol;
    struct Node *next;
};

// Function to add a symbol to the linked list
void addToSet(struct Node **set, char symbol) {
    // Check if symbol already exists in the set
    struct Node *temp = *set;
    while (temp != NULL) {
        if (temp->symbol == symbol) {
            return; // Symbol is already in the set
        }
        temp = temp->next;
    }
    
    // If not found, add symbol to the linked list
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->symbol = symbol;
    newNode->next = *set;
    *set = newNode;
}

// Function to print the linked list
void printSet(struct Node *set) {
    struct Node *temp = set;
    while (temp != NULL) {
        printf("%c ", temp->symbol);
        temp = temp->next;
    }
}

// Function to find the FIRST set for a given non-terminal
void findFirst(char c, struct Node **firstSet) {
    int i, j;
    if (!isupper(c)) {
        // If it's a terminal, add it directly to the FIRST set
        addToSet(firstSet, c);
        return;
    }
    
    // Check each production of the non-terminal
    for (i = 0; i < n; i++) {
        if (productions[i][0] == c) {
            for (j = 3; j < strlen(productions[i]); j++) {
                if (productions[i][j] == '|') break;  // Handle multiple productions
                if (isupper(productions[i][j])) {
                    // Recursively calculate the FIRST set of non-terminals
                    findFirst(productions[i][j], firstSet);
                } else {
                    // Add terminal to FIRST set
                    addToSet(firstSet, productions[i][j]);
                }
            }
        }
    }
}

// Function to find the FOLLOW set for a given non-terminal
void findFollow(char c, struct Node **followSet) {
    int i, j;

    // If the non-terminal is the start symbol, add '$' to its FOLLOW set
    if (productions[0][0] == c)
        addToSet(followSet, '$');

    for (i = 0; i < n; i++) {
        for (j = 3; j < strlen(productions[i]); j++) {
            if (productions[i][j] == c) {
                if (productions[i][j + 1] != '\0') {
                    // Add the FIRST set of the next symbol in the production
                    findFirst(productions[i][j + 1], followSet);
                } else if (c != productions[i][0]) {
                    // If the current non-terminal is at the end, add FOLLOW of the left-hand non-terminal
                    findFollow(productions[i][0], followSet);
                }
            }
        }
    }
}

int main() {
    int i, j;
    char choice, c;
    
    // Input number of terminals and their symbols
    printf("Enter the number of terminals: ");
    scanf("%d", &t);
    printf("Enter the terminals: ");
    scanf("%s", terminals);
    
    // Input number of non-terminals and their symbols
    printf("Enter the number of non-terminals: ");
    scanf("%d", &nt);
    printf("Enter the non-terminals: ");
    scanf("%s", nonterminals);
    
    // Input number of productions and the actual production rules
    printf("Enter the number of productions: ");
    scanf("%d", &n);

    // Dynamically allocate memory for productions
    productions = (char **)malloc(n * sizeof(char *));
    for (i = 0; i < n; i++) {
        productions[i] = (char *)malloc(MAX * sizeof(char));
        scanf("%s", productions[i]);
    }
    
    // Input the start symbol
    printf("Enter the start symbol: ");
    scanf(" %c", &c);

    // Arrays to store FIRST and FOLLOW sets for each non-terminal
    struct Node **firstSets = (struct Node **)malloc(nt * sizeof(struct Node *));
    struct Node **followSets = (struct Node **)malloc(nt * sizeof(struct Node *));
    
    for (i = 0; i < nt; i++) {
        firstSets[i] = NULL;
        followSets[i] = NULL;
    }

    // Compute FIRST set for the start symbol
    printf("First(%c) = {", c);
    findFirst(c, &firstSets[0]);
    printSet(firstSets[0]);
    printf("}\n");

    // Compute FOLLOW set for the start symbol
    printf("Follow(%c) = {", c);
    findFollow(c, &followSets[0]);
    printSet(followSets[0]);
    printf("}\n");

    // Free allocated memory for productions and sets
    for (i = 0; i < n; i++) {
        free(productions[i]);
    }
    free(productions);
    free(firstSets);
    free(followSets);

    return 0;
}
