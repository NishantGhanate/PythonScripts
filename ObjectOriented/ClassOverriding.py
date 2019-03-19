class Parent:
    
    def main(self):
        print("Hi from paret")

# Inherting Parent class  
class Child(Parent):

    # Overrding parent class function
    def main(self):
        print("Hi from child")

object = Child()
object.main()

# Output
# Hi from child