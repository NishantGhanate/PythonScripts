# Encapsulation
# An objects variables should not always be directly accessible.
# To prevent accidental change, an objects variables can sometimes 
# only be changed with an objects methods. Those type of variables are private variables.
# The methods can ensure the correct values are set. If an incorrect value is set, 
# the method can return an error.

class Tau:
    def __init__(self):
        self.__version = 21
    def getVersion(self):
        print(self.__version)
    def setVersion(self,version):
        self.__version = version
    
obj = Tau()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)

# Output 
# 21
# 23
# Traceback (most recent call last):
#   File "h:\Github\PythonScripts\ObjectOriented\Encapsulation.py", line 13, in <module>
#     print(obj.__version)
# AttributeError: 'Tau' object has no attribute '__version