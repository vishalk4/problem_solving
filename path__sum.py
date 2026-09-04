# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        # check if the current node is a leaf node a leaf node has no left or right child
        if root.left is None and root.right is None:
            # return true if the remaining target equals the value of this leaf node
            return targetSum == root.val
        # subtract the current node value from targetSum
        remainingSum = targetSum - root.val
        # check with recursion that the remaining sum exists in either the left subtree or right subtree
        return (self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum))
