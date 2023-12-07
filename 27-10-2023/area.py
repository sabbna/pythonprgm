#laambda to find the area of square rectangle & triangle

a=int(input("enter the side of the sqaure \n"))
area= lambda b:b*b
print("area of sqaure",area(a))

a=int(input("enter the length of rectangle \n"))
b=int(input("enter the breadth of rectangle \n"))
area= lambda l,b:l*b
print("area of rectangle is",area(a,b))


a=int(input("enter the height of triangle \n"))
b=int(input("enter the breadth of triangle \n"))
area= lambda h,b:h*b
print("area of triangle is",area(a,b))
