a=int(input("enter the year"))
if(a%4==0) & (a%100!=0) | (a%400==0):
    print("the year is leap")
else:
    print("not a leap year")
