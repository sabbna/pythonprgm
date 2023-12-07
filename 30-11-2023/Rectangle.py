#Create Rectangle class with attributes length and breadth and methods to find area and
#perimeter. Compare two Rectangle objects by their area.


class Rectangle():
    
    def __init__(self,l,w):
        self.length=l
        self.breadth=w
    def rectangle_area(self):
        return self.length*self.breadth
    def rectangle_peri(self):
        return 2*(self.length+self.breadth)

rectangle1=Rectangle(12,10)
rectangle2=Rectangle(6,5)

print("Area1=",rectangle1.rectangle_area())
print("Area2=",rectangle2.rectangle_area())
print("Perimeter1=",rectangle1.rectangle_peri())
print("Perimeter2=",rectangle2.rectangle_peri())

if(rectangle1.rectangle_area()==rectangle2.rectangle_area()):
    print("Area are Equal")
else:
    print("Area are not Equal")
