from Mypackage import mod1
from Mypackage import mod2
from Mypackage import mod3

m=int(input("enter the first number"))
n=int(input("enter the second number"))
s=mod1.sum(m,n)
print("sum",s)
a=mod2.avg(m,n)
print("average",a)
p1=mod3.power(m)
print("power of",m,"is",p1)
p2=mod3.power(n)
print("power of",n,"is",p2)
