# this program get 3 values and return maximum values
x = input("enter number1 :")
y = input("enter number2 :")
z = input("enter number3 :")

# find max from 2 number
# =========================
if int(x) > int(y):
    temp = x
else:
    temp = y
# =========================
if int(temp) >= int(z):
    print("max is : ", temp)
else:
    print("max is : ", z)
# =========================
