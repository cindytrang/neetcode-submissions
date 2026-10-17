# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder starts from left part of the root, then root somewhere and then right part of the root
        # stack of the values 

        # preorder would tell us straight away the root of the tree, so we want to build three tree from the root 
        # 3 9 15 20
        # Preorder: [3, 9, 20, 15, 7]
        # Inorder: [9, 3, 15, 20, 7]
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])

        return root        

        
        