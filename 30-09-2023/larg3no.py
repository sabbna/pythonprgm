print("enter 3 number")
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num3 and num1> num2:
    print(num1,"is the greater")
elif num1> num3:
    print(num2,"is the greater")
else:
     print(num3,"is the greater")
