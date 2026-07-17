# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def m_d(root): # function to check maximum depth
            if root is None:
                return 0
            
            left = m_d(root.left) # recursive function to check maximum left depth
            right = m_d(root.right) # recursive function to check maximum right depth
            
            return 1 + max(left, right) # returning the max depth
        return m_d(root)
