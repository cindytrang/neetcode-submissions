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
        oldToNew[node] = Node(node.val)
        dq = deque([node]) 
        while dq:
            curr = dq.popleft()
            for n in curr.neighbors:
                # neighbor is not explore
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    dq.append(n)
                #neighbor explored
                oldToNew[curr].neighbors.append(oldToNew[n])
        return oldToNew[node]

        