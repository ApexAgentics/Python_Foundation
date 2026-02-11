
# ============================================================
# TOPIC: Type Casting (Type Conversion)
# ============================================================

# ------------------------------------------------------------
# DEFINITION:
# Type casting converts one data type into another.
# Python provides built-in functions for this.
# ------------------------------------------------------------

# Implicit Casting (automatic)
x = 10       # int
y = 2.5      # float

result = x + y   # int automatically converted to float
print(result)
print(type(result))

# ------------------------------------------------------------
# Explicit Casting (manual)
# ------------------------------------------------------------

num_str = "100"

num_int = int(num_str)   # Convert string to integer
print(num_int)
print(type(num_int))

# Convert to float
num_float = float(num_str)
print(num_float)

# Convert number to string
num_string = str(50)
print(num_string)
print(type(num_string))

# Boolean casting rules
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("text"))  # True

# ------------------------------------------------------------
# COMMON ERRORS:
# Invalid conversion raises ValueError
# int("abc")  # Uncomment to see error
# ------------------------------------------------------------

# ------------------------------------------------------------
# IMPORTANT CONCEPT:
# Type casting does NOT modify original variable unless reassigned.
# ------------------------------------------------------------
