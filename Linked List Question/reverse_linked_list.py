class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head 
            while curr.next:
                curr = curr.next 
            curr.next = newNode 


    def display(self):
        curr = self.head 
        while curr:
            print(curr.data,end = ' ')
            curr=curr.next 
    def reverse(self):
        curr = self.head 
        prev = None
        while curr:
            Next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = Next 
        self.head = prev 
       
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.display()
print()
LL.reverse()
print("Reverse the Linked List: ")
LL.display()
