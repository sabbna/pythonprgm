#program to find factorial of a number using factorial

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter the number:"))
print("the factorial of",n,"is",factorial(n))
