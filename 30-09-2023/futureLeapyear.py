a = int(input("enter current year"))
b = int(input("enter future year"))
for i in range(a,b+1):
    if i%4==0 and i%100!=0 or i%400==0 :
        print(i)
