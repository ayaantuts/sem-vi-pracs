key = 'BATTLE'
ROUNDS = 2
def transposition_d(plain_text:str) -> list:
	plain_text = plain_text.replace(' ', '').upper()
	rows = len(plain_text) // len(key)
	if len(plain_text) % len(key) != 0:
		rows += 1

	plain_text += (rows * len(key) - len(plain_text)) * 'Z'
	columns = [''] * len(key)
	for i in range(len(key)):
		for j in range(rows):
			columns[i] += plain_text[i + j * len(key)]
	return columns

def encrypt(transposeD:list) -> str:
	cipher_text = ''
	for i in sorted(key):
		cipher_text += transposeD[key.index(i)]
	return cipher_text

def decrypt(transposeD:list) -> str:
	plain_text = ''
	for i in range(len(transposeD[0])):
		for j in range(len(key)):
			plain_text += transposeD[j][i]
	return plain_text

plain_text = 'SUCCESS IS NOT FINAL FAILURE IS NOT FINAL'
for i in range(ROUNDS):
	transposeD = transposition_d(plain_text)
	print('Transpose D:', transposeD)

cipher_text = encrypt(transposeD)
print('Cipher text:', cipher_text)
plain_text = decrypt(transposeD)
print('Plain text:', plain_text)