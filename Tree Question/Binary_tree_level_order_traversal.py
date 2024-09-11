from collections import deque

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
def Level_order_traversal(root):
    result = []
    if root is None:
        return result 
    
    q = deque([root])
    while q:
        q_size = len(q)
        level = [] 
        for i in range(q_size):
            curr_node = q.popleft()
            level.append(curr_node.data)

            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        result.append(level)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(Level_order_traversal(root))
