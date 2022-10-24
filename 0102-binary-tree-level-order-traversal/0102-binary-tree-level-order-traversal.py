# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        cur = [root]
        children = []
        output = []
        while cur:
            output.append([n.val for n in cur])
            for n in cur:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            cur = children
            children = []
        return output
                    
            
        