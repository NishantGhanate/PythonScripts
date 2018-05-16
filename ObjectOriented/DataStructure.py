class Que:
    def __init__(self , contents):
        self._hiddenlist = list(contents)

    def push(self,value):
        self._hiddenlist.insert(0 , value)
        print(self._hiddenlist)

    def pop(self):
        if len(self._hiddenlist):
            self._hiddenlist.pop(0)
            print(self._hiddenlist)
        else:
            print("Empty Que")
        
que = Que([1, 2.25, 3.0, 4, 1234.5])
que.push(0)
que.pop()


class Node:
    def __init__(self, dataValue ):
        self.dataValue = dataValue
        self.nextValue = None

class Slink:
    def __init__(self):
        self.headValue = None

    def printLink(self):
        printval = self.headValue
        while printval is not None:
            print (printval.dataValue)
            printval = printval.nextValue
    
    def atStart(self,newData):
        NewNode = Node(newData)
        NewNode.nextValue = self.headValue
        self.headValue = NewNode

# lis = Slink()
# lis.atStart("Sun")
# lis.atStart("Mon")
# lis.printLink()  


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,dataValue):
        self.stack.append(dataValue)
        return self.stack

    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return "This value pop =" +self.stack.pop()

# stack = Stack()
# stack.push("1")
# stack.push("2")
# stack.push("3")
# print(stack.pop())
# print(stack.push("5"))




