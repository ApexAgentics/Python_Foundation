
# ============================================================
# TOPIC: Multiple Assignment in Python
# ============================================================

# ------------------------------------------------------------
# DEFINITION:
# Multiple assignment allows assigning multiple variables
# in a single line of code.
# ------------------------------------------------------------

# Assign multiple values at once
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# ------------------------------------------------------------
# VALUE SWAPPING (WITHOUT TEMP VARIABLE)
# ------------------------------------------------------------

a = 5
b = 10

# Python automatically handles tuple packing/unpacking
a, b = b, a

print("a:", a)
print("b:", b)

# ------------------------------------------------------------
# HOW IT WORKS INTERNALLY:
# Python first creates a tuple on the right:
# (b, a)
# Then unpacks it into variables on the left.
# ------------------------------------------------------------

# Extended unpacking
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)

# '*' collects remaining values into a list

# ------------------------------------------------------------
# WHEN TO USE:
# - Swapping variables
# - Returning multiple values from functions
# - Unpacking sequences
# ------------------------------------------------------------
