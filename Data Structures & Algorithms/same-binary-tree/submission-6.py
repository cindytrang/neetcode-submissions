# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both are empty
            return True
        if not p or not q:
            return False
        def isSameSubtree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False 
            return tree1.val == tree2.val and isSameSubtree(tree1.left, tree2.left) and isSameSubtree(tree1.right, tree2.right)

        return isSameSubtree(p,q) 
            