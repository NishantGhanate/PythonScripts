from abc import ABCMeta, abstractmethod

"""The term metaprogramming refers to the potential for a program to have knowledge of or manipulate itself. 
Python supports a form of metaprogramming for classes called metaclasses."""

class Color(metaclass=ABCMeta):
    @abstractmethod
    def fillColor(self):
        pass

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def colorIt(self):
        pass

# Inheriting & override fillcolor 
class RedColor(Color):
    def fillColor(self):
        print("red color")

class BlueColor(Color):
    def fillColor(self):
        print("blue color")

# Super : builtin returns a proxy object (temporary object of the superclass) 
# that allows us to access methods of the base class.
class Rectangle(Shape):
    def __init__(self, color):
        super(Rectangle, self).__init__(color)

    def colorIt(self):
        print("Rectangle filled with ", end="")
        self.color.fillColor()

class Circle(Shape):
    def __init__(self, color):
        super(Circle, self).__init__(color)

    def colorIt(self):
        print("Circle filled with ", end="")
        self.color.fillColor()

if __name__ == '__main__':
    s1 = Rectangle(RedColor())
    s1.colorIt()

    s2 = Circle(BlueColor())
    s2.colorIt()

