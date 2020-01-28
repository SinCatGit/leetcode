import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/binary-tree-maximum-path-sum/

        Given a non-empty binary tree, find the maximum path sum.
        For this problem, a path is defined as any sequence of nodes from some starting node to any node
        in the tree along the parent-child connections. The path must contain at least one node
        and does not need to go through the root.

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        int

        Examples
        --------
        >>> node1=TreeNode(1)
        >>> node2=TreeNode(2)
        >>> node3=TreeNode(3)
        >>> node1.left=node2
        >>> node1.right=node3
        >>> solution = Solution()
        >>> solution.maxPathSum(node1)
        6
        >>> node_10 = TreeNode(-10)
        >>> node9 = TreeNode(9)
        >>> node20 = TreeNode(20)
        >>> node_10.left = node9
        >>> node_10.right = node20
        >>> node15 = TreeNode(15)
        >>> node7 = TreeNode(7)
        >>> node20.left = node15
        >>> node20.right = node7
        >>> solution.maxPathSum(node_10)
        42

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=WicS0ANkAdY&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m&index=2
        .. [2] https://www.youtube.com/watch?v=9ZNky1wqNUw
        """

        def dfs(r):
            if not r:
                return 0
            left = max(dfs(r.left), 0)
            right = max(dfs(r.right), 0)
            self.ans = max(self.ans, r.val+left+right)
            return r.val + max(left, right)

        dfs(root)
        return int(self.ans)



