class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
    

def detet_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

# Creating a loop resulting in the linked list:
# 10 -> 20 -> 30 -> 40 -> 10 -> 20 -> 30 ...
head.next.next.next.next = head
print(detet_cycle(head))