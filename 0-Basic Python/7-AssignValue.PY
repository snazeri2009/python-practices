# how to assign value to variable

X = "VALUE1"
Y = "VALUE2"
Z = "VALUE3"

# ==================================
x, y, z = "aa", "bb", "cc"
x, y, z = "VALUE1", "VALUE2", "VALUE3"
print(x, y, z)
# ================================== Same values
x = "T"
Y = "T"
Z = "T"

X = Y = Z = "T"
x = y = z = "SAME VALUE"
print(x, y, z)
# ==================================
# packed Value
packed = ["test1", "test2", "test3"]
x, y, z = packed  # unpack value to three variable
print(x, y, z)
# ==================================
# this code has this Error  : too many values to unpack (expected 2)  Why ?
packed = ["test1", "test2", "test3"]
x, y = packed
print(x, y, z)
# ==================================
