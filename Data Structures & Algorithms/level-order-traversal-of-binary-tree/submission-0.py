# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order which is BFS
        if not root:
            return []
        
        # init queue
        dq = deque([root])
        adj_nested = []

        while dq:
            lvl_nodes = []
            for _ in range(len(dq)):
                node = dq.popleft()
                lvl_nodes.append(node.val)
                if node.left: # always ensure there is a val
                    dq.append(node.left)
                if node.right: 
                    dq.append(node.right)
            adj_nested.append(lvl_nodes)

        return adj_nested
                
