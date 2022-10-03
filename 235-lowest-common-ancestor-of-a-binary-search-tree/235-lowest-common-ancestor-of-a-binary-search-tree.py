# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recurse(self, node, p, q, seenP, seenQ):
        if node == None:
            return None, seenP, seenQ
    
        lca_l, sp_l, sq_l = self.recurse(node.left, p, q, seenP, seenQ)
        lca_r, sp_r, sq_r = self.recurse(node.right, p, q, seenP, seenQ)
        
        if lca_l:
            return lca_l, sp_l, sq_l
        if lca_r:
            return lca_r, sp_r, sq_r
        
        sp = sp_l or sp_r or node == p
        sq = sq_l or sq_r or node == q
        
        if sp and sq:
            return node, True, True
        
        return None, sp, sq
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', seenP=False, seenQ=False) -> 'TreeNode':
        node, _, _ = self.recurse(root, p, q, False, False)
        return node
        
        
            
        
        
        