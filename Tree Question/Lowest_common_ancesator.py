class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

def LCA(root,p,q):
    if root is None:
        return None 
    if root.data == p.data or root.data == q.data:
        return root.data 
    
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)

    if left is not None and right is not None:
        return root.data 
    
    return left if left is not None else right 

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)

root.right.left = Node(0)
root.right.right = Node(8)

root.left.right.left = Node(7)
root.left.right.right = Node(4)

p = root.left 
q = root.right
print("Lowest common Ancestor: ")
print(LCA(root,p,q))

    
