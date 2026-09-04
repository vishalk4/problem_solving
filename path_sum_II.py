# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, remaining, path):
            if not node:
                return
            # Aad the current node to the path
            path.append(node.val)
            # check if we reached a leaf node
            if not node.left and not node.right:
                # check the complete path equals targetsum
                if remaining == node.val:
                    result.append(path[:])  # Store a copy of the path
            else:
                # explore left and right subtrees
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            # backtrack: remove the current node before returning
            path.pop()
        dfs(root, targetSum, [])
        return result
