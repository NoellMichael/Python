#reverse a number
num = int(input("enter the number to be reversed: "))
temp = num
reverse = 0
while num>0:
    remainder = num%10
    reverse = (reverse*10)+remainder
    num = num//10
print("the reversed number is: ",reverse)