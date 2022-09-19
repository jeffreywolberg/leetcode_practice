# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], checkingSubtree=False) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if root.val == subRoot.val and self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def sameTree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        
        if s.val == t.val: return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        else:
            return False
    
    
    
    
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], checkingSubtree=False) -> bool:
#         if root is None and subRoot is None:
#             return True
#         elif not root or not subRoot:
#             return False
        
#         if root.val == subRoot.val:
#             root_same = self.checkEquality(root, subRoot)
#         else:
#             root_same = False
            
#         l_same = self.isSubtree(root.left, subRoot)
#         r_same = self.isSubtree(root.right, subRoot)
        
#         return l_same or r_same or root_same
        
        
#     def checkEquality(self, root, subRoot):
#         if not root and not subRoot:
#             return True
#         elif not root or not subRoot:
#             return False
#         elif root.val != subRoot.val:
#             return False
        
#         l_same = self.checkEquality(root.left, subRoot.left)
#         r_same = self.checkEquality(root.right, subRoot.right)
        
#         return l_same and r_same
        
        
            
            
        