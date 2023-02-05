# ==================================================== Section 1
str1 = input("Enter Main String  :  ")
str2 = input("Enter String To Find In Main String :  ")
print(str2 in str1)  # return true if exists otherwise return false
# soheila is a student
# oheila
# ==================================================== Section 2
print("*******************")
str1 = input("Enter Main String : ")
str2 = input("Enter String To Find In Main String :")
print(str2 not in str1)   # return true if not exists otherwise return false

# ==================================================== Section 3
print("*******************")
str1 = input("Enter Main String : ")
str2 = input("Enter String To Find In Main String :")
# i want show message that is exists or not exists
if str2 in str1:  # true
    print(str2 + " on " + str1 + " is ")
else:
    print(str2 + " not on " + str1 + " is ")
# ====================================================
