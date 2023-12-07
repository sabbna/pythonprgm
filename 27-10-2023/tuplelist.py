#convert a tuple into list and add items

t=(1,2,3,4,5)
print(t)
l=list(t)
a=int(input("enter item to add \n"))
l.append(a)
t=tuple(l)
print(t)
