print("this program show max number betweem 2 numbers ")
a = int(input("enter number 1 :"))
b = int(input("enter number 2 :"))
##################################
if b > a:
    print("max is ", b)
else:
    print("max is ", a)

# Short Hand If
if a > b:
    print("a is greater than b")
##################################
print("A") if a > b else print("B")  # short if else  in python
##################################
"""
logical operator  or and not
if a > b or a > c:   one of the conditions is true return true
if a > b and a > c:  all the conditions are true return true    
if not  a > b :  not convert result if a is less than b return true  10>2 === true === not true ==false   ,20>30 ==false not false ==true
"""
# Nested If
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")  # if x >10 and x>20
    else:
        print("but not above 20.")  # if x >10 and x<=20
else:
    print("Below ten")
########################
