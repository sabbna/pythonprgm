#generate fibonacci series of N terms

n=int(input("No.of terms"))
n1,n2 = 0,1
count=0
if n<=0:
    print("Enter a positive integer ")
elif n==1:
    print("Fibonacci series upto n",":")
    print(n2)
else:
    print("Fibonnacci sequence:")
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1
