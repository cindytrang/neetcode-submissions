# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left < root
        # root < right
        # children of left < root 

        # we have to check the whole tree so that is On minimum 
        
        # BFS and DFS, dfs is a good solution but it uses the stack which can be expensive when we use rescursion calls so that relies on memory more
        # with BFS approch we can use the queue, stack can go to size on but with queue it can be also on 

        if not root: # first edge case
            return True
        
        dq = deque([(root, float('-inf'), float('inf'))])
        while dq:
            for _ in range(len(dq)):
                node, lower_bound, upper_bound = dq.popleft()
                if node.val >= upper_bound or node.val <= lower_bound:
                    return False
                if node.left:
                    dq.append((node.left, lower_bound, node.val))
                if node.right:
                    dq.append((node.right, node.val, upper_bound))
        return True


        