# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            # create a node using the middle element
            root = TreeNode(nums[mid])
            # use recursion to build the left subtree
            root.left = buildBST(left, mid - 1)
            # use recursion to build the right subtree
            root.right = buildBST(mid + 1, right)
            # return the root of this subtree
            return root
        return buildBST(0, len(nums) - 1)
