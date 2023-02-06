strTest = " this is a Test "

print("lower case ", strTest.lower())  # convert string to lower case
print("upper case ", strTest.upper())  # convert string to upper case


print("LENGTH IS  ", len(strTest))     # get length of string
strTest = strTest.strip()   # The empty space on the left and right side is removed
# get length of string after removing   spaces from left and right side
print("LENGTH IS   ", len(strTest))

################
a = "this is a test  program"
print(a.replace("H", "J"))  # replace  "J" with "H"
################
a = "this ,is a test,  program"
print(a.split(","))  # returns ['this', ' is',...]  list of strings

################
a = " this is a test  program"  # remove left space
print(a.lstrip())
################
a = " this is a test  program  "
print(a.rstrip())  # remove right space
################
# returns a string with the first letter of each word capitalized and all other letters in lowercase
txt = "Welcome to my world"
x = txt.title()
print(x)
########################
# this code get string from user and  and remove spaces from left and right side and for any characters in the string print *
strTest = input("Enter your string without space : ").strip()
# strTest = strTest.strip()
for ch1 in strTest:
    print("*")
########################
