#fibonacci using recursion
def Fibo(n):
    if n<0:
        print("Incorrect input")
#1st Fibonacci number is 0
    elif n==0:
        return 0
#2nd Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)

#Main Program
print(Fibo(9))