EPSILON = "ε"
DOLLAR = "$"
grammar = {
	"X": ["ABC"],
	"A": ["a", EPSILON],
	"B": ["b", EPSILON],
	"C": ["c", "d"]
}

START_VAR = "X"
first = {}
follow = {}

def find_first(prod:str) -> set:
	if prod in first:
		return first[prod]
	first[prod] = set()
	if prod in grammar:
		for production in grammar[prod]:
			if production[0].islower():
				first[prod].add(production[0])
			elif production[0] in grammar:
				while EPSILON in production:
					first[prod] |= find_first(production[0])
					production = production[1:]
				if EPSILON in first[production[0]]:
					first[prod] |= first[production[0]] - {EPSILON}
			else:
				first[prod].add(production[0])
	return first[prod]

for prod in grammar:
	find_first(prod)

print("First:", first)
# print("Follow:", follow)
