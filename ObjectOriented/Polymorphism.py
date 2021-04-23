import math 

# Parent Class
class Shape:
    def __init__(self , color='Red', filled = False):
        self.color = color
        self.filled = filled
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.__color = color
    def get_filled(self):
        return self.filled
    def set_filled(self,filled):
        self.filled = filled

# Children class 1 
class Rectangle(Shape):

    def __init__(self,length,breadth):
        # Refers to parent class constructer
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self,length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth
    
    def set_breadth(self, breadth):
        self.__breadth = breadth
    
    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)

# Children class 2
class Circle(Shape):

    def __init__(self,radius):
        super().__init__()
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self,radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius **2

    def get_perimeter(self):
        return 2 * math.pi*self.__radius

r1 = Rectangle(11,2.5)
print("Area of rectangle r1 : " , r1.get_area() )
print("Perimeter of rectangle r1 : " , r1.get_perimeter() )
print("Color of rectangle r1 =  ",r1.get_color() )
print("Is rectangle r1 filled : ",r1.get_filled() )
r1.set_filled(True)
print("Is rectangle r1 filled :" , r1.get_filled() )
r1.set_color("Orange")
print("Color of rectangle r1 " , r1.get_color() )

c1 = Circle(12)
print("\nArea of circle c1 : ",format(c1.get_area() ))
print("perimeter of circle c1 : ",format(c1.get_perimeter() ))
print("Is circle c1 filled : ",c1.get_color() )
print("Is circle c1 filled : ",c1.get_filled() )
c1.set_color(True)   
print("Is circle c1 filled : ",c1.get_filled() )
c1.set_color("Blue")
print("Color of circle c1 : ",c1.get_color() )  


# Output

# Area of rectangle r1 :  27.5
# Perimeter of rectangle r1 :  27.0
# Color of rectangle r1 =   Red
# Is rectangle r1 filled :  False
# Is rectangle r1 filled : True
# Color of rectangle r1  Red

# Area of circle c1 :  452.3893421169302
# perimeter of circle c1 :  75.39822368615503
# Is circle c1 filled :  Red
# Is circle c1 filled :  False
# Is circle c1 filled :  False
# Color of circle c1 :  Red