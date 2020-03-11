class Car(object):

    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()
    
    def factory2(type):
        try:
            return eval(type + "()")
        except :
            print('Inavlid car type')

    # Static method does not depends on the class instance
    # https://www.programiz.com/python-programming/methods/built-in/staticmethod
    factory = staticmethod(factory)
    factory2 = staticmethod(factory2)

class Racecar(Car):
    def drive(self):
        print("Racecar driving.")

class Van(Car):
    def drive(self):
        print("Van driving.")

# Create object using factory.
obj = Car.factory("Racecar")
obj.drive()

obj = Car.factory2("Van")
obj.drive()

