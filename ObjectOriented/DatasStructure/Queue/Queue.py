
# In Queue DataStructure general rule is : First in / First Out  


class Queue:
    def __init__(self,arr):
        self.arr = arr
       
    def enque(self,value): 
        self.arr.append(value)
        return self.arr

    def deque(self):
        self.arr.pop(0)
        return self.arr

if __name__ == '__main__':
    ls = list(map(int,input().rstrip().split()))
    queue = Queue(ls)
    print('Queue = {}'.format(queue))
    print('Enque = {}'.format(queue.enque(9)))
    print('Deque = {} '.format(queue.deque()))

    