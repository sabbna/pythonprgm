class car:
    def __init__(self,color,price,km):
        self.color=color
        self.price=price
        self.km=km
    def __add__(self,other):
        return self.km+other.km
    def __gt__(self,other):
        if(self.price>other.price):
            return True
        else:
            return False
c1=car("red",200000,34)
c2=car("white",300000,24)
sum=c1.km+c2.km
print("sum of kilometers of two cars:",sum)
if(c1.price>c2.price):
    print("car1 is more expensive than car2")
else:
    print("car2 is more expensive than car1")
