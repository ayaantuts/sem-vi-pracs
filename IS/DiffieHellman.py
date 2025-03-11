# Implementation of Diffie-Hellman
# Persons: Alice and Bob
p = int(input("Enter the value of p: "))
g = int(input("Enter the value of g: "))

# Alice
a = int(input("Enter the value of a: "))
x = int(pow(g, a, p))

# Bob
b = int(input("Enter the value of b: "))
y = int(pow(g, b, p))

# Key Generation
print("Alice sends: ", x)
print("Bob sends: ", y)

# Alice
ka = int(pow(y, a, p))
print("Alice's Secret Key: ", ka)

# Bob
kb = int(pow(x, b, p))
print("Bob's Secret Key: ", kb)