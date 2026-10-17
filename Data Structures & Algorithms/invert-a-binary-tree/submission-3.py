# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # depth of values level doesnt change, we want to explore at level
        # at each step we swap two values (so we have two choices)

        # task is to find correct values and swap them recursively 
        # DFS
        if not root:
            return None
        def dfs(node):
            # keep exploring
            if node is None:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            # do nothing no two choices
        dfs(root)
        return root