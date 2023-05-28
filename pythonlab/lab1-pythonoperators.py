# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a % b = {a % b}")  # Modulus
print(f"a // b = {a // b}")  # Floor Division
print(f"a ** b = {a ** b}")  # Exponentiation

# Comparison Operators
x = 5
y = 7
print("\nComparison Operators:")
print(f"x < y is {x < y}") #less than
print(f"x > y is {x > y}") #greater than
print(f"x == y is {x == y}") #assigning values
print(f"x != y is {x != y}") #not equal
print(f"x <= y is {x <= y}") #less than or equal to
print(f"x >= y is {x >= y}") #greater than or equal to

# Assignment Operators
print("\nAssignment Operators:")
c = 15
c += 5  # c = c + 5
print(f"c = {c}")
c -= 3  # c = c - 3
print(f"c = {c}")
c *= 2  # c = c * 2
print(f"c = {c}")
c /= 4  # c = c / 4
print(f"c = {c}")
c %= 5  # c = c % 5
print(f"c = {c}")
c **= 3  # c = c ** 3
print(f"c = {c}")

# Logical Operators
p = True
q = False
print("\nLogical Operators:")
print(f"p and q is {p and q}")
print(f"p or q is {p or q}")
print(f"not p is {not p}")

# Bitwise Operators
m = 10  # Binary: 1010
n = 7   # Binary: 0111
print("\nBitwise Operators:")
print(f"m & n = {m & n}")  # Bitwise AND
print(f"m | n = {m | n}")  # Bitwise OR
print(f"m ^ n = {m ^ n}")  # Bitwise XOR
print(f"~m = {~m}")  # Bitwise NOT
print(f"m << 2 = {m << 2}")  # Bitwise Left Shift
print(f"m >> 2 = {m >> 2}")  # Bitwise Right Shift

# Membership Operators
list_a = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print(f"2 in list_a is {2 in list_a}")
print(f"6 not in list_a is {6 not in list_a}")

# Identity Operators
x = 10
y = 10
z = [1, 2, 3]
print("\nIdentity Operators:")
print(f"x is y is {x is y}")
print(f"x is not z is {x is not z}")