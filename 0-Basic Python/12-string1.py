# The first character has index 0.
# ==================================================== Section 1
str1 = input("Enter String : ")
for a in str1:  # for example when user enter soheila program print ****** 7 start
    print("*")
# ==================================================== Section 2
str1 = input("Enter String : ")
for a in str1:  # for example when user enter soheila program  s o h e i l a vertical line
    print(a)
# ==================================================== Section 3
str1 = "SOHEILA NAZERI"
print(str1)
# ==================================================== Section 4
# 1 start end 4  # str1[1],str1[2], str1[3], str1[4]
print("1---- str1[1:5]   : " + str1[1:5])
print("2---- str1[:5]    : " + str1[:5])  # 0 start end 4
print("3---- str1[2:]    : " + str1[2:])  # index 2 to   end
print("4---- str1[-5:-1] : " + str1[-5:-1])  # from -1 to -5  soheila a is -1
print("5---- str1[2:3]   : " + str1[2:3])  # from 2 to 2
print("6---- str1[-1:]   : " + str1[-1:])  # test ???
print("7---- str1[-5:2] : " + str1[-5:])  # test ???
