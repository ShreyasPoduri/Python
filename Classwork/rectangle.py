class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length*self.width
    
newRectangle = Rectangle(10,12)
print("Dimensions of rectangle - length : %d  width : %d" %(newRectangle.length , newRectangle.width))
print("Area of rectangle = ", newRectangle.rectangle_area())