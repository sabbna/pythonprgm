n=int(input("enter the value on n:"))
fact=1
if n<0:
    print("no exist")
elif n==0:
    print("1")
else:
    for i in range(1,n+1):
        fact=1*fact
print(n,"!=",fact)
