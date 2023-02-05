# this code show type of variable
####################################
x = 10  # int
print("type of x is : ", type(x), " value is :", x)

x = "string_1"  # string
print("type of x is : ", type(x), " value is :", x)

x = "string_2"  # string
print("type of x is : ", type(x), " value is :", x)

x = 10.25  # float
print("type of x is : ", type(x), " value is :", x)

# you can Change value of a variable in python

####################################
x = 10
#print ("value is",X)
a = 10
#print ("value is",A)


s = str(3.5) + str(5.2)  # 3.55.2

x = str(3) + str(5)  # 35

y = int("3") + int("4")  # 7

z = float("4.5")+float("3.5")  # 8.0


print("s is:", s, "x is:", x, " y is :", y, " z is:", z)


# for input value from users you can use the input function
x = input("ENTER VALUE  :")

print("float is :", float(x))
print("int is :", int(x))
print("str is :", str(x))


x = input("enter number1 :")
y = input("enter number2 :")


print(int(x)+int(y))  # int
print(x+y)  # string

# python shows an Error  why ?
print(int(x)+y)  # int + str


# show data  type
print("data type is :", type(10.25))  # float
print("data type is :", type(10))  # int
print("data type is :", type("10.25"))  # string
print("data type is :", type("abc"))  # string
print("data type is :", type(10.36))  # float
