# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(node, prev, first, second):
            if not node:
                return prev, first, second
            # traverse left subtree
            prev, first, second = inorder(node.left, prev, first, second)
            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            prev = node
            # traverse right subtree
            return inorder(node.right, prev, first, second)
        prev, first, second = inorder(root, None, None, None)
        # Swap the two incorrect nodes
        first.val, second.val = second.val, first.val
