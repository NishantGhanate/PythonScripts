registry = {}

class MultiMethod(object):

    def __init__(self,name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)    
    
    def register(self,types,function):
        self.typemap[types] = function

def overload(*types):
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types,function)
        return mm
    return register

@overload(int, int)
def area(length, breadth):
    calc = length * breadth
    print (calc)
    
@overload(int)
def area(size):
    calc =  size * size
    print (calc)
    
area(3) # returns 9
area(4,5) # returns 20
