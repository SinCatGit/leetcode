
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.longest_path = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/longest-univalue-path/

        Given a binary tree, find the length of the longest path where each node in the path has the same value.
        This path may or may not pass through the root.

        The length of path between two nodes is represented by the number of edges between them.

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        int

        Examples
        --------
        >>> node1=TreeNode(5)
        >>> node2=TreeNode(4)
        >>> node3=TreeNode(5)
        >>> node4=TreeNode(1)
        >>> node5=TreeNode(1)
        >>> node6=TreeNode(5)
        >>> node1.left=node2
        >>> node1.right=node3
        >>> node2.left=node4
        >>> node2.right=node5
        >>> node3.right=node6
        >>> solution = Solution()
        >>> solution.longestUnivaluePath(node1)
        2

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=yX1hVhcHcH8
        """
        def dfs(r):
            if not r:
                return 0
            left = dfs(r.left)
            right = dfs(r.right)
            pleft, pright = 0, 0
            if r.left and r.val == r.left.val:
                pleft += left + 1
            if r.right and r.val == r.right.val:
                pright += right + 1
            self.longest_path = max(self.longest_path, pleft+pright)
            return max(pleft, pright)

        dfs(root)

        return self.longest_path

