# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root, depth) -> int:
        if root == None:
            return depth
        
        d1 = self.recurse(root.right, depth+1)
        d2 = self.recurse(root.left, depth+1)
        
        return max(d1, d2)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0)
        
        