class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def merge_sorted_linked_list(l1,l2):
    dummy = current = Node(-1) 
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1 
            l1 = l1.next
        else:
            current.next = l2 
            l2 = l2.next 
        current = current.next 

    current.next = l1 or l2 
    return dummy.next 

def display(head):
    while head:
        print(head.data, end = '->')
        head = head.next 
    print()

#1 -> 3 -> 5 -> None, 2 -> 4 -> 6 -> None
l1 = Node(1) 
l1.next = Node(3)
l1.next.next = Node(5) 

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

head = merge_sorted_linked_list(l1,l2)
display(head)
