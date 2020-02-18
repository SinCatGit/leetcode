from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        https://leetcode.com/problems/leaf-similar-trees/

        Consider all the leaves of a binary tree.  From left to right order,
        the values of those leaves form a leaf value sequence.

        For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

        Two binary trees are considered leaf-similar if their leaf value sequence is the same.

        Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

        Note:

        Both of the given trees will have between 1 and 100 nodes.

        Parameters
        ----------
        root1: TreeNode
        root2: TreeNode

        Returns
        -------
        bool

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/leaf-similar-trees/discuss/152329/C%2B%2BJavaPython-O(H)-Space

        """
        stack1 = list()
        res1 = list()
        while root1 or stack1:
            if root1:
                stack1.append(root1)
                root1 = root1.left
            else:
                root1 = stack1.pop()
                if not root1.left and not root1.right:
                    res1.append(root1.val)
                root1 = root1.right

        stack2 = list()
        res2 = list()
        while root2 or stack2:
            if root2:
                stack2.append(root2)
                root2 = root2.left
            else:
                root2 = stack2.pop()
                if not root2.left and not root2.right:
                    res2.append(root2.val)
                root2 = root2.right

        return res1 == res2







