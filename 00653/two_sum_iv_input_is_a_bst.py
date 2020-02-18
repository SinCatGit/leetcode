from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

        Given a Binary Search Tree and a target number, return true if there exist
        two elements in the BST such that their sum is equal to the given target.

        Example 1:

        Input:
            5
           / \
          3   6
         / |   \
        2   4   7

        Target = 9

        Output: True


        Example 2:

        Input:
            5
           / \
          3   6
         / |   \
        2   4   7

        Target = 28

        Output: False

        Parameters
        ----------
        root: TreeNode
        k: int

        Returns
        -------
        bool

        Examples
        --------

        References
        ---------

        """
        stack = list()
        visited = set()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if k - root.val in visited:
                    return True
                visited.add(root.val)
                root = root.right
        return False












