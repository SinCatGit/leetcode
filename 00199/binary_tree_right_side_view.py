from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-right-side-view/

        Given a binary tree, imagine yourself standing on the right side of it,
        return the values of the nodes you can see ordered from top to bottom.

        Parameters
        ----------
        root: Node

        Returns
        -------
        List[int]

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms

        """
        level = [root]
        res = list()
        while root and level:
            res += level[-1].val,
            level = [k for node in level for k in (node.left, node.right) if k]
        return res
