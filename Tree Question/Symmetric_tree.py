class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

def isSymmetric(root1,root2):
    if root1 is None and root2 is None:
        return True 
    if root1 is None or root2 is None:
        return False 
    
    return root1.data == root2.data and isSymmetric(root1.left,root2.right) and isSymmetric(root1.right,root2.left)

def Symmetric(root):
    return isSymmetric(root,root)

root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(4)

root.right.left = Node(4)
root.right.right = Node(3)

print("Is the tree symmetric :")
print(Symmetric(root))