from os import *
from sys import *
from collections import *
from math import *

class Queue :
  
    def __init__(self) -> None:
        self.queue : list= []


    def isEmpty(self) :
        if len(self.queue) > 0:
            return False 
        return True

    def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.queue.append(data)


    def dequeue(self) :
        #Implement the dequeue() function
        dq = self.front()
        if dq !=-1:
            self.queue.pop(0)
        return dq

    def front(self):
        if self.isEmpty():
            return -1
        return self.queue[0]


q = Queue()
q.enqueue(12)
q.enqueue(22)
q.enqueue(42)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.front())
print(q.dequeue())
q.enqueue(1)
print(q.front())
