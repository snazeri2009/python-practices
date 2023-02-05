# Booleand data type
# ================================
print(10 > 9)
print(10 == 9)
print(10 < 9)
# ================================
a = bool("hello")
if a == True:
    print("string is true")
# ================================
print("#######################")
print(bool("Hello"))
print(bool(0))
print(bool(3))
print(bool(-9))
print(bool(""))
print(bool("        "))

# ================================
"""
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
