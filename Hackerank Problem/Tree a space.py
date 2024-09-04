""" question : 
You are given a complete, balanced N-Ary Tree and must support Q queries. There are 3 kinds of queries. Return true or false depending on whether the query was successful.

Lock(v, id) - Lock vertex v for user - id
Unlock(v, id) - If vertex v is locked by the same id, unlock it.
Upgrade(v, id) - If v is unlocked and has at least one locked vertex in it's subtree and every locked vertex in the subtree of v is locked by id, unlock them and lock v instead.
Further, here are some additional constraints

A vertex cannot be locked if it has any locked ancestors or descendants, by any ID.
When a vertex is upgraded, it's locked descendants are automatically unlocked.
An upgrade operation is not possible if the vertex is already locked or has any locked ancestors
An unlock operation is only possible if the vertex is already locked and locked by the same id
P.S. - The question was very badly stated and not a single constraint was mentioned openly on the problem statement. A lot of these constraints had to be deduced by supplying custom input and observing the expected output. There were no constraints on the size of the variables.
The problem without the constraint of the ID and Upgrade function is well known and explained here.
          World
        /       \
       /          \
     /             \
   Asia            Africa
  /    \          /       \
China  India    South     Egypt
                Africa
"""

import math

class Node:
    def __init__(self,val):
        self.val = val 
        self.uid = None 
        self.parent = None 
        self.children = []
        self.isLocked = False 
        self.isDescendantLocked = 0 

class Tree:
    def __init__(self,n, m, node_lst,queries):
        self.node_lst = []
        self.node_map = {}
        for node in node_lst:
            self.node_lst.append(Node(node))
            self.node_map[node] = Node(node)

        for i in range(int(n/m)):
            start = i * m + 1
            end = i * m +m 
            if end > n - 1:
                end -= end % (n -1)
            if end < n:
                self.node_lst[i].children = self.node_lst[start:end + 1] 
        for i in range(1,n):
            self.node_lst[i].parent = self.node_lst[math.ceil(i/m) - 1]
        self.root = self.node_lst[0]
        self.processed_queries = [query.split() for query in queries]
    
    def lock(self,node,uid):
        if node.isDescendantLocked > 0 or node.isLocked or self.isAncestorLocked(node.parent):
            return False 
        node.uid = uid 
        node.isLocked = True 
        parent_node = node.parent

        while parent_node:
            parent_node.isDescendantLocked += 1
            parent_node = parent_node.parent 
        return True 

    def unlock(self,node, uid):
        if uid != node.uid or not node.isLocked:
            return False 
        
        node.isLocked = False 
        node.uid = None 
        parent_node = node.parent 

        while parent_node:
            parent_node.isDescendantLocked -= 1
            parent_node = parent_node.parent 
        return True 
    
    def upgrade(self,node,uid):
        if node.isDescendantLocked == 0 or self.isAncestorLocked(node.parent):
            return False 
        
        self.unlockChildren(node, uid)
        self.lock(node,uid)
        return True 

    def isAncestorLocked(self,node):
        while node:
            if node.isLocked:
                return True 
            node = node.parent 
        return False 
    
    def unlockChildrean(self,node,uid):
        for child in node.children:
            self.unlock(child,uid)
            self.unlockChildrean(child,uid)

    def print_tree(self,node,out):
        out += node.val + "No of Descendants Locked: " + str(node.isDescendantLocked) + " is Node Locked : " + str(node.isLocked) +",\n"
        for child in node.children:
            out = self.print_tree(child,out)
        return out 

    def __str__(self):
        return self.print_tree(self.root,'')
n = 7 # no of nodes 
m = 2 # To create m-ary tree
nodes = ['World', 'Asia', 'Africa', 'China', 'India','South Africa','Egypt']
queries = ["1 China 9", '1 India 9', '3 Asia 9', '2 India 9', ' 2 Asia 9']
obj = Tree(n, m, nodes, queries)
res = []
for query in obj.processed_queries:
    if query[0] == "1":
        res.append(obj.lock(obj.node_map[query[1]], query[2]))
    elif query[0] == "2":
        res.append(obj.unlock(obj.node_map[query[1]], query[2]))
    elif query[0] == "3":
        res.append(obj.upgrade(obj.node_map[query[1]], query[2]))

print(res)