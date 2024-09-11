class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def intersect_point_in_linkedlist(headA, headB):
    currA = headA 
    currB = headB
        
    while currA != currB:
        currA = headB if not currA else currA.next 
        currB = headA if not currB else currB.next 
    return currA

def display(head):
    while head:
        print(head.data, end = '->')
        head = head.next 
    print()


#[4,1,8,4,5],
headA = Node(10)
headA.next = Node(15)
headA.next.next = Node(30)

 # Creation of the second list
headB = Node(3)
headB.next = Node(6)
headB.next.next = Node(9)
headB.next.next.next = headA.next 


head = intersect_point_in_linkedlist(headA,headB)
display(headA)
display(headB)
print(head.data)