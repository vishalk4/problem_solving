# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # case 1: If both nodes are none both trees are the same at this position
        if not p and not q:
            return True

        # case 2: if one node is none and the other is not the trees are different
        if not p or not q:
            return False

        # case 3: if the values of the current nodes are different the trees are not the same
        if p.val != q.val:
            return False

        # apply recurssion for every node
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
