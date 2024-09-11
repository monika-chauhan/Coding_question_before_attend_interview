class Queue:
    def __init__(self):
        self.s1 = [] 
        self.s2 = []
    
    def enqueue(self,x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    
    def deQueue(self):
        if len(self.s1) == 0:
            return -1 
        x = self.s1[-1]
        self.s1.pop()
        return x 

    def display(self):
        return self.s1
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.deQueue()
print(q.display())


