from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

        Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

        A node in this binary tree can be flipped by swapping the left child and the right child of that node.

        Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a
        sequence of N values the voyage of the tree.

        (Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse
        the left child, then preorder-traverse the right child.)

        Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage
        we are given.

        If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

        If we cannot do so, then return the list [-1].

        Parameters
        ----------
        root: TreeNode
        voyage: List[int]

        Returns
        -------
        List[int]

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/discuss/214216/JavaC%2B%2BPython-DFS-Solution

        """
        self.i = 0
        self.res = list()

        def dfs(r):
            if not r:
                return True
            if r.val != voyage[self.i]:
                return False
            self.i += 1
            if r.left and r.left.val != voyage[self.i]:
                self.res.append(r.val)
                r.left, r.right = r.right, r.left
            return dfs(r.left) and dfs(r.right)

        return self.res if dfs(root) else [-1]

















