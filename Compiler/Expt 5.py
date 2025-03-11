# Operator Precedence Grammar
# take the terminals
terminals = ['+', '-', '*', '/', '(', ')', 'id', '$']

# create the table
def create_table():
	table = {}
	for i in terminals:
		table[i] = {}
		for j in terminals:
			table[i][j] = ''
	return table

def get_precedence(op):
	if op == '$':
		return -1
	if op == '+' or op == '-':
		return 1
	if op == '*' or op == '/':
		return 2
	if op == '(':
		return 3
	if op == ')':
		return 3
	if op == 'id':
		return float('inf')

# fill the cells
def fill_cell(table, row, col):
	rowP = get_precedence(row)
	colP = get_precedence(col)
	if rowP > colP:
		table[row][col] = '>'
	elif rowP < colP:
		table[row][col] = '<'
	else:
		if row == 'id':
			table[row][col] = ' '
		elif row == '^':
			table[row][col] = '<'
		else:
			table[row][col] = '>'

# fill the table
def fill_table(table):
	for i in terminals:
		for j in terminals:
			fill_cell(table, i, j)

# print the table
def print_table(table):
	print(' ', end = ' ')
	for i in terminals:
		print(i, end = ' ')
	print()
	for i in terminals:
		print(i, end = ' ')
		for j in terminals:
			print(table[i][j], end = ' ')
		print()

table = create_table()
fill_table(table)
print_table(table)