from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/find-bottom-left-tree-value/

        Given a binary tree, find the leftmost value in the last row of the tree.

        Example 1:
        Input:

            2
           / \
          1   3

        Output:
        1
        Example 2:
        Input:

                1
               / \
              2   3
             /   / \
            4   5   6
               /
              7

        Output:
        7
        Note: You may assume the tree (i.e., the given root node) is not NULL.

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-%2B-Java)

        """
        node = root
        q = [root]
        while q:
            node = q.pop(0)
            q += filter(None, [node.right, node.left])

        return node.val







