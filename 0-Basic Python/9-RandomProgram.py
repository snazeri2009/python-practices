# this program with random functions create numbers between 1 and 4
# then get two numbers from user and return + , - , * , /
import random
print(" THIS IS A RANDOM PROGRAM ")

a = random.randrange(1, 4)   # create a random number from 1 to 4

# a = random.randrange(1, 5,2)   # 1,3,5
# a = random.randrange(1, 10,3)     # 1,4,7,10

# ================================

print(" RANDOM NUMBER IS : ", a)

x = input("Enter Number 1 :")
y = input("Enter Number 2 :")
# ================================
if a == 1:
    print("Sum is :", int(x)+int(y))
elif a == 2:
    print("MINUS is :", int(x)-int(y))
elif a == 3:
    print("MULTI is :", int(x)*int(y))
elif a == 4:
    print("DIVIDE is :", int(x)/int(y))

# ==========================
