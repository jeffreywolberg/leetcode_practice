import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTRec(self, root, upper=math.inf, lower=-math.inf):
        if not root:
            return True
        if root.val >= upper or root.val <= lower:
            return False
        
        return self.isValidBSTRec(root.right, upper, root.val) and self.isValidBSTRec(root.left, root.val, lower)
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
#         if root.left and root.left.val >= root.val:
#             return False
#         if root.right and root.right.val <= root.val:
#             return False
        
        return self.isValidBSTRec(root)
        