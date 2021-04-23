
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

# Excution starts from here in python
if __name__ == "__main__":

    # Initlizing Class
    roger = Dog("Roger",5)

    # Calling Class function
    print(roger.description())

    # Passing argument to class function
    print(roger.speak("affermative"))


# output
# Roger is 5 years old
# Roger says affermative

