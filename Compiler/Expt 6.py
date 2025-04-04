# Constructing DAG from input string
# Input: a + a * (b - c) + (b - c) * d

import re

def get_operands(exp):
	operands = re.findall(r'[a-zA-Z]', exp)
	return operands

def get_operators(exp):
	operators = re.findall(r'[-+*/]', exp)
	return operators

def get_nodes(exp):
	nodes = re.findall(r'[a-zA-Z+-/*]', exp)
	return nodes

def get_edges(exp):
	edges = []
	for i in range(len(exp)):
		if exp[i] in ['+', '-', '*', '/']:
			edges.append((exp[i], exp[i-1], exp[i+1]))
	return edges

def get_dag(exp):
	nodes = get_nodes(exp)
	edges = get_edges(exp)
	dag = {}
	for i in range(len(edges)):
		if edges[i][0] not in dag:
			dag[edges[i][0]] = [edges[i][1], edges[i][2]]
		else:
			dag[edges[i][0]].append(edges[i][1])
			dag[edges[i][0]].append(edges[i][2])
	return dag

def main():
	exp = input("Enter the expression: ")
	operands = get_operands(exp)
	operators = get_operators(exp)
	nodes = get_nodes(exp)
	edges = get_edges(exp)
	dag = get_dag(exp)
	print("Operands: ", operands)
	print("Operators: ", operators)
	print("Nodes: ", nodes)
	print("Edges: ", edges)
	print("DAG: ", dag)

if __name__ == '__main__':
	main()