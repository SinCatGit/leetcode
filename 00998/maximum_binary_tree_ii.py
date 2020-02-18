from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        """
        https://leetcode.com/problems/maximum-binary-tree-ii/

        We are given the root node of a maximum tree: a tree where every node
        has a value greater than any other value in its subtree.

        Just as in the previous problem, the given tree was constructed from an
        list A (root = Construct(A)) recursively with the following Construct(A) routine:

        If A is empty, return null.
        Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
        The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
        The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
        Return root.
        Note that we were not given A directly, only a root node root = Construct(A).

        Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

        Return Construct(B).


        Parameters
        ----------
        root: TreeNode
        val: int

        Returns
        -------
        TreeNode

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/maximum-binary-tree-ii/discuss/242936/JavaC%2B%2BPython-Recursion-and-Iteration

        """
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node

    def insertIntoMaxTreeV01(self, root: TreeNode, val: int) -> TreeNode:
        b_node = TreeNode(val)
        if not root:
            return b_node

        if root.val < val:
            b_node.left = root
            return b_node

        res = root
        parent = None
        while root and root.val > val:
            parent = root
            root = root.right
        parent.right = b_node
        b_node.left = root

        return res









