from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        [298. Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence)

        Given a binary tree, find the length of the longest consecutive sequence path.


        The path refers to any sequence of nodes from some starting node to any node in the tree along
        the parent-child connections. The longest consecutive path need to be from parent to child
        (cannot be the reverse).

        For example,

        ```
           1
            \
             3
            / \
           2   4
                \
                 5
        ```

        Longest consecutive sequence path is `3-4-5`, so return `3`.

        ```
           2
            \
             3
            /
           2
          /
         1
        ```

        Longest consecutive sequence path is `2-3`,not`3-2-1`, so return `2`.


        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1]
        .. [2]
        .. [3]

        """
        ret = 0
        stack = [(root, 1)]

        while stack:
            node, cnt = stack.pop()
            left, right = node.left, node.right
            if right:
                stack.append((right, cnt+1 if right.val == node.val+1 else 1))
            if left:
                stack.append((left, cnt+1 if left.val == node.val+1 else 1))

            ret = max(ret, cnt)

        return ret
