from typing import List
from heapq import heappop, heappush


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        [366. Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/)

        Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all
        leaves, repeat until the tree is empty.

        **Example:**

        ```
        Input: [1,2,3,4,5]

                  1
                 / \
                2   3
               / \
              4   5

        Output: [[4,5,3],[2],[1]]
        ```

        **Explanation:**

        1. Removing the leaves `[4,5,3]` would result in this tree:

        ```
                  1
                 /
                2
        ```

        2. Now removing the leaf `[2]` would result in this tree:

        ```
                  1
        ```

        3. Now removing the leaf `[1]` would result in the empty tree:

        ```
                  []
        ```

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        List[List[int]]

        Examples
        --------

        """
        self.res = []

        def dfs(r):
            if not r:
                return 0
            h = max(dfs(r.left), dfs(r.right)) + 1
            if h > len(self.res):
                self.res.append([])
            self.res[h-1].append(r.val)
            return h

        dfs(root)

        return self.res
