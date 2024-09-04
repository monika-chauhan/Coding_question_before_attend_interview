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
    
    def remove_nth_node_from_end(self,pos):
        left = self.head 
        right = self.head 
        i = 0 
        while i < pos:
            right = right.next
            i += 1 
       
        if not right:
            return self.head.next
        
        while right and right.next:
            left = left.next
            right = right.next 
        left.next = left.next.next
        return self.head



    def display(self):
        curr = self.head 
        while curr:
            print(curr.data,end = ' ')
            curr = curr.next 

LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.display()
print()
LL.remove_nth_node_from_end(3)
print("Remove the node from end of the Linked List: ")
LL.display()


        