# Processing a String One Character at a Time
# Problem :
# You want to process a string one character at a time.
# We don't have character type in python as we know,
# so we can use string like a list and iterate them in for loop statement.
#
name = "Mohammad"
for char in name:
    # do something
    print(char)

# or in the for clause of a list comprehension
upper_name = [char.upper() for char in name]
print(upper_name)

# You can call a function on each
# character with the map built-in function
upper_name_method_2 = map(str.upper, name)
for item in upper_name_method_2:
    print(item)
