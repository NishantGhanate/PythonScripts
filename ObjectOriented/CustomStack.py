class StabCode:
    
    def __init__(self):
        self.stack = []

    def StabLaugh(self,value):
        self.stack.append(value)
        print(self.stack)
        
    def StabCry(self):
        del self.stack[-1]
        print(self.stack)

if __name__ == '__main__':
    bc =  StabCode()
    bc.StabLaugh(5)
    bc.StabLaugh(6)
    bc.StabCry()