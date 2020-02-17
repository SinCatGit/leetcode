class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    pre = None

    def isValidBST(self, root: TreeNode) -> bool:
        """
        https://leetcode.com/problems/validate-binary-search-tree/

        Given a binary tree, determine if it is a valid binary search tree (BST).

        Assume a BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.


        Example 1:

            2
           / \
          1   3

        Input: [2,1,3]
        Output: true
        Example 2:

            5
           / \
          1   4
             / \
            3   6

        Input: [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        bool

        Examples
        --------

        """
        def inner_valid(r, down=float('-inf'), up=float('inf')) -> bool:
            if not r:
                return True

            return down < r.val < up and inner_valid(r.left, down, r.val) \
                   and inner_valid(r.right, r.val, up)

        return inner_valid(root)

    def isValidBSTV01(self, root: TreeNode) -> bool:
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if self.pre is not None and root.val <= self.pre:
                    return False
                self.pre = root.val
                root = root.right
        return True




