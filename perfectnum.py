#perfect number
#A perfect number is a positive integer that is equal to the sum of its proper divisors
num = int(input("enter any number: "))
sumdiv = 0
for i in range(1, num):
    if(num % i == 0):
        sumdiv = sumdiv + 1
if (sumdiv == num):
        print("the number is a perfect number")
else:
        print("the number is not a perfect number")
        
