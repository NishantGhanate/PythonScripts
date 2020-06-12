import time
import threading

class threadtester (threading.Thread):
    def __init__(self, id, name, i):
       threading.Thread.__init__(self)
       self.id = id
       self.name = name
       self.i = i
       
    def run(self):
       self.thread_test(self.name, self.i, 5)
       print ("%s has finished execution " %self.name)

    def thread_test(self,name, wait, i):
        while i:
            time.sleep(wait)
            print ("Running %s \n" %name)
            i = i - 1

if __name__=="__main__":
    n = 5
    thread1 = [None] * n 
    for i in range(n):
        thread1[i] = threadtester(1, "First Thread", 1)
        thread1[i].start()

    ##  Join will will wait till threads are completed 
    # thread1.join()
    # thread2.join()
    # thread3.join()