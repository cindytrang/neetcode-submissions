"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        oldToNew = {}

        #DFS
        def dfs(node):
            if node in oldToNew: #explored
                return oldToNew[node]
            #non explored and add it to explored
            copy = Node(node.val)
            oldToNew[node] = copy 

            #check all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


        