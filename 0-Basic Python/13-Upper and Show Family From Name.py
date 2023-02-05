
# this Program Get name from users and check name in program and show Family
str1 = input("ENTER YOUR NAME : ")
# if user enter soheila we must upper or lower and check because user maybe enter soheila Soheila SOHEILA ,...
str1 = str1.upper()
if str1 == "SOHEILA":
    print("Your Family is Nazeri")
elif str1 == "samira".upper():  # why ?
    print("Your Family is AHMADI")
elif str1 == "Sima".upper():  # it is ok to write  : elif str1 == "SIMA": why ?
    print("Your Family is  Larizade")
elif str1 == "Sara".upper():
    print("Your Family is  Hoseini")
elif str1 == "nasrin".upper():
    print("Your Family is Koliyayi")
elif str1 == "SOROUSH".upper():
    print("Your Family is  Sehat")
else:
    print("wrong!")
