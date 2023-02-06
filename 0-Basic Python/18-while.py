# when you want to create a loop you should use the while statement,for,...
# while loop :   counter,condtitions,increment counter,...
i = 1   # 1 to 5   Initial value
# this code print 1 to 6 number
while i < 6:  # condition
    print(i)
    i += 1  # increment counter
################
i = 0   # 0,2,4,6,8,10,12,14 to 98 # initial  value
while i < 100:  # condition
    print(i)
    i += 2   # increment counter
################
i = 1  # ebtedayi   #sum 10 number  # initial  value
# The user enters the numbers
while i <= 10:  # condition
    # begin
    b = input("enter number")
    sum += b   # sum=sum+b
    i += 1   # increment counter
    # end
 # after enter the numbers print sum of the numbers
print("sum ten number is ", sum)
################
# this program get ten numbers for sum but if the number is <0 then break
i = 1  # Initial value

while i <= 10:  # condition
    b = input("enter number")
    if b < 0:
        break  # break for break and exit from loop or use continue to continue
    sum += b
    i += 1  # increment counter
print("sum [" + str(i-1) + "] number is " + sum)
################
# print 1,2,3,4  when arrived to 5 then break  and exit while
i = 1  # Initial value
while i < 6:  # condition
    print(i)
    i += 1  # increment counter
    if i == 5:
        break  # When its value is 5 break and exit from loop
else:
    print("i is no longer less than 6")  # else will execute ???

####################
