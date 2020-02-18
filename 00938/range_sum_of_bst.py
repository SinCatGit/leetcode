from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        https://leetcode.com/problems/range-sum-of-bst/

        Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

        The binary search tree is guaranteed to have unique values.



        Example 1:

        Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
        Output: 32
        Example 2:

        Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
        Output: 23


        Note:

        The number of nodes in the tree is at most 10000.
        The final answer is guaranteed to be less than 2^31.

        Parameters
        ----------
        root: TreeNode
        L: int
        R: int

        Returns
        -------
        int

        Examples
        --------

        References
        ---------

        """
        res = 0
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if L <= root.val <= R:
                    res += root.val
                root = root.right
        return res

















