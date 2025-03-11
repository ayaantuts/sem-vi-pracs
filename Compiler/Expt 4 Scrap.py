# Predictive Parser for the given grammar
# S -> aAd | bBc
# A -> a | ε
# B -> b | ε

first = {}
follow = {}
predict = {}
grammar = {
	'S': ['aAd', 'bBc'],
	'A': ['a', 'ε'],
	'B': ['b', 'ε']
}

def find_first(symbol:str) -> list:
	if symbol in first:
		return first[symbol]
	first[symbol] = []
	for production in grammar[symbol]:
		if production[0].islower():
			first[symbol].append(production[0])
		elif production[0] in grammar:
			first[symbol] += find_first(production[0])
		else:
			first[symbol].append(production[0])
	return first[symbol]

def find_follow(symbol:str) -> list:
	if symbol in follow:
		return follow[symbol]
	follow[symbol] = []
	if symbol == 'S':
		follow[symbol].append('$')
	for LHS, RHS in grammar.items():
		for production in RHS:
			if symbol in production:
				index = production.index(symbol)
				if index == len(production) - 1:
					if LHS != symbol:
						follow[symbol] += find_follow(LHS)
				else:
					if production[index + 1].islower():

						follow[symbol].append(production[index + 1])
					elif production[index + 1] in grammar:
						follow[symbol] += find_first(production[index + 1])
					else:
						follow[symbol].append(production[index + 1])
	return follow[symbol]

def LL1(string):
	stack = ['$', 'S']
	string += '$'
	i = 0
	while stack[-1] != '$':
		if stack[-1] == string[i]:
			# convert stack to string
			print("".join(stack), string[i:])
			stack.pop()
			i += 1
		else:
			if stack[-1] in grammar:
				print("".join(stack), string[i:])
				for production in predict[stack[-1]]:
					if string[i] in first[stack[-1]]:
						stack.pop()
						for j in range(len(production) - 1, -1, -1):
							stack.append(production[j])
						break
					elif 'ε' in first[stack[-1]]:
						stack.pop()
						break
				else:
					return False
			else:
				return False
	return True

def main():
	for key in grammar:
		find_first(key)
		find_follow(key)
		find_predict(key)
	print('First:', first)
	print('Follow:', follow)
	print('Predict:', predict)
	string = input('Enter the string: ')
	if LL1(string):
		print('String is accepted')
	else:
		print('String is rejected')

if __name__ == '__main__':
	main()