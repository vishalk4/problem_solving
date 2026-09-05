class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        # empty tree and a single node each have 1 possible BST
        dp[0] = 1
        dp[1] = 1
        for nodes in range(2, n + 1):
            # try every node as the root
            for root in range(1, nodes + 1):
                # number of nodes on the left side
                left = root - 1
                # number of nodes on the right side
                right = nodes - root
                # multiply all left and right subtrees
                dp[nodes] += dp[left] * dp[right]
        return dp[n]
