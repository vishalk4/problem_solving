# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def isMirror(left, right):
            # if both nodes are none they are symmetric
            if left is None and right is None:
                return True
            # if only one node is none they are not symmetric
            if left is None or right is None:
                return False
            # 1.both nodes have the same value
            # 2.left subtree of left node matches right subtree of right node
            # 3.right subtree of left node matches left subtree of right node
            return (left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left))
        # compare the left and right subtrees of the root
        return isMirror(root.left, root.right)
