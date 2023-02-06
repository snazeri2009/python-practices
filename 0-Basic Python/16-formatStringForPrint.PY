name = "soheila"
family = "nazeri"
age = 37
txt = "My name is {}, my family is {} , i am {} years old "  # format string for print
print(txt.format(name, family, age))

#txt ="my name is " + name + " and my family is " +family + "my age is " + age
txt = "My name is {1}, my family is {0} , i am {2} years old "
print(txt.format(family, name, age))


# \n new line , \t tab
# {0} =name, {1} =family, {2} =age
txt = " my name is {0} \n and my family is  {1} \n  \t my Age is {2} "
print(txt.format(name, family, age))
