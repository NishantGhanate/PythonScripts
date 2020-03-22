import random 

# MAGIC METHOD'S 

class Chaos:

    def __init__(self,x):
        self.x = x
        self.reasons = ['ola' , 'bhola', 'achu']
    def __add__(self,arg):
        return self.x - arg.x
    
    def __sub__(self,arg):
        return random.choice(self.reasons)
    
    def __gt__(self,arg):
        if self.x > arg.x:
            return 'Oh'
        else:
            return 'Acha'
    
    def __eq__(self, arg): 
        return random.choice(self.reasons)
    
    def __invert__(self):
        return (' ~ nah ')


if __name__ == "__main__":
    
    richard = print

    c = Chaos(6)
    d = Chaos(9)

    richard( c + d )
    richard(c < d )
    richard( c > d )
    richard( c == d )
    richard( ~ c )