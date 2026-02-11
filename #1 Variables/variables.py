
# ============================================================
# TOPIC: Variables in Python
# ============================================================

# ------------------------------------------------------------
# DEFINITION:
# A variable is a named reference to an object stored in memory.
# Python is dynamically typed, meaning you do NOT declare the type.
# The type is inferred automatically at runtime.
# ------------------------------------------------------------

# Basic variable assignments
name = "Alice"          # String (str)
age = 25                # Integer (int)
height = 5.6            # Float (float)
is_student = True       # Boolean (bool)

# Python determines the type automatically
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# ------------------------------------------------------------
# HOW VARIABLES WORK INTERNALLY:
# - Python creates an object in memory.
# - The variable name becomes a reference to that object.
# - Multiple variables can reference the same object.
# ------------------------------------------------------------

a = 10
b = a   # Both reference the same integer object (10)

print(id(a))  # Memory address of object
print(id(b))  # Same memory address

# Reassigning creates a new object reference
a = 20
print(id(a))  # New memory address
print(id(b))  # Still points to old object

# ------------------------------------------------------------
# NAMING RULES:
# - Must start with letter or underscore
# - Cannot start with number
# - Case-sensitive
# - Cannot use reserved keywords
# ------------------------------------------------------------

valid_name = "OK"
_valid = "OK"
# 2invalid = "NO"  # SyntaxError

# ------------------------------------------------------------
# BEST PRACTICES:
# - Use descriptive names
# - Follow snake_case convention
# - Avoid single-letter names unless in loops
# ------------------------------------------------------------
