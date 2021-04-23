
class Dog:

    # Class attribute
    species = 'mammal'

    # Class Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Class function/method
    def description(self):
        return "{} is {} years old".format(self.name,self.age)
    
    def speak(self,sound):
        return "{} says {}".format(self.name,sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):

    def run(self,speed):
        return "{} runs {}".format(self.name,speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Excution starts from here in python
if __name__ == "__main__":

    # Child classes inherit attributes and
    # behaviors from the parent class
    jim = Bulldog("Jim", 12)
    print(jim.description())

    print(jim.speak("Roger that"))
    # Child classes have specific attributes
    # and behaviors as well
    print(jim.run("Light speed"))

    # Is jim an instance of Dog()?
    print(isinstance(jim, Dog))

# Output
# Jim is 12 years old
# Jim says Roger that
# Jim runs Light speed
# True