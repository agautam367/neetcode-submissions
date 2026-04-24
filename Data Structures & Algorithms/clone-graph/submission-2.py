"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old = {}
        def dfs(node):
            if node in old:
                return old[node]
            newNode = Node(node.val)
            old[node]=newNode
            for i in node.neighbors:
                newNode.neighbors.append(dfs(i))
            return newNode
            print(newNode.neighbors)
        if node:
            return dfs(node)
        else:
            return None
        