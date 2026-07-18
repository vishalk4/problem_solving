# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left) # it computes left height
            if left == -1:
                return -1

            right = height(node.right) # it computes right height
            if right == -1:
                return -1

            if abs(left - right) > 1: #comparing right heights
                return -1

            return 1 + max(left, right) # return ing the final height with first node

        return height(root) != -1
