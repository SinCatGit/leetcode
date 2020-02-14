from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        """
        https://leetcode.com/problems/construct-string-from-binary-tree/

        You need to construct a string consists of parenthesis and integers from a binary tree
        with the preorder traversing way.

        The null node needs to be represented by empty parenthesis pair "()". And you need to omit
        all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between
        the string and the original binary tree.

        Parameters
        ----------
        t: TreeNode

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice
        .. [2] https://www.youtube.com/watch?v=5IAq5jd8O7Y

        """
        def dfs(root: TreeNode) -> str:
            if not root:
                return ''
            res = str(root.val)
            if root.left:
                res += f'({dfs(root.left)})'

            if root.right:
                if not root.left:
                    res += f'()({dfs(root.right)})'
                else:
                    res += f'({dfs(root.right)})'
            return res
        return dfs(t)

