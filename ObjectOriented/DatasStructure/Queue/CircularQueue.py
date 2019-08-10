

class CircularQueue:

    def __init__(self,size):
        self.size = size

        # initializing queue with none 
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1

    def enqueue(self, data): 
        # condition if queue is full 
        if ((self.rear + 1) % self.size == self.front):  
            return (" Queue is Full\n") 
           
        # Checking if queue is  empty 
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else:      
            # next position of rear 
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data 
    
    def dequeue(self): 
        # Checking if queue is  empty 
        if (self.front == -1):
            return ("Queue is Empty\n") 
        # condition for only one element 
        elif (self.front == self.rear):  
            temp = self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp

    def display(self): 
      
        #  Checking if queue is  empty 
        if(self.front == -1):  
            return ("Queue is Empty") 

        print("Elements in the circular queue are:",  end = " ") 
        for i in range(self.front, self.rear + 1): 
            print(self.queue[i], end = " ")     


if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()
    print(cq.enqueue(6))
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    print(cq.dequeue())