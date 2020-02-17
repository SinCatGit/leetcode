
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0
    min_val = float('inf')

    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        https://leetcode.com/problems/closest-binary-search-tree-value/

        Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

        Note:

        Given target value is a floating point.
        You are guaranteed to have only one unique value in the BST that is closest to the target.

        Parameters
        ----------
        root: TreeNode
        target: float

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70327/4-7-lines-recursiveiterative-RubyC%2B%2BJavaPython

        """
        res = root.val
        while root:
            if abs(res-target) >= abs(root.val-target):
                res = root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return res

    def closestValueV01(self, root: TreeNode, target: float) -> int:

        def dfs(r):
            if not r:
                return
            dfs(r.left)
            if abs(r.val-target) < self.min_val:
                self.min_val = abs(r.val-target)
                self.res = r.val
            dfs(r.right)

        dfs(root)

        return self.res






