class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 



def max_depth_of_tree(root):
    if root is None:
        return 0 

    left = max_depth_of_tree(root.left)
    right = max_depth_of_tree(root.right)

    return  1 + max(left,right)
root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(2)

print("Diameter of the Binary Tree: ")
print(max_depth_of_tree(root))
