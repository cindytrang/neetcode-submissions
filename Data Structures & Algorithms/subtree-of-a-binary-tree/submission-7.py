# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True 
        if self.isSimilar(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSimilar(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node2 is None or node1 is None:
            return False
        return node1.val == node2.val and self.isSimilar(node1.left, node2.left) and self.isSimilar(node1.right, node2.right)