class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

def is_valid(root):
    mini = float('-inf')
    maxi = float('inf')
    def is_valid_helper(node, mini, maxi):
        if node is None:
            return True

        # False if this node violates min/max constraint
        if node.data < mini or node.data > maxi:
            return False

        # Otherwise check the subtrees recursively
        # tightening the min or max constraint
        return (is_valid_helper(node.left, mini, node.data - 1) and
                is_valid_helper(node.right, node.data+1, maxi))
        
    return is_valid_helper(root,mini,maxi)


root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(4)

print(is_valid(root))

