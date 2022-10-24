# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return self.countNodes(root.left)  + self.countNodes(root.right) + 1
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        l = self.countNodes(root.left)
        r = self.countNodes(root.right)
        
        if k > l+1:
            v = self.kthSmallest(root.right, k-l-1)
            return v
        elif k <= l:
            v = self.kthSmallest(root.left, k)
            return v
        else:
            return root.val
        
        