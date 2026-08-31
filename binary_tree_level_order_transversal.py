# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        # queue is used to process nodes level by level
        queue = deque([root])
        while queue:
            # number of nodes present in the current level
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                # remove the node from the front of the queue
                node = queue.popleft()
                # add the node value to the current level
                current_level.append(node.val)
                # add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
