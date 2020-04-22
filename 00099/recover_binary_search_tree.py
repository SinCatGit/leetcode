class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        #### [99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

        Two elements of a binary search tree (BST) are swapped by mistake.

        Recover the tree without changing its structure.

        **Example 1:**

        ```
        Input: [1,3,null,null,2]

           1
          /
         3
          \
           2

        Output: [3,1,null,null,2]

           3
          /
         1
          \
           2
        ```

        **Example 2:**

        ```
        Input: [3,1,4,null,null,2]

          3
         / \
        1   4
           /
          2

        Output: [2,1,4,null,null,3]

          2
         / \
        1   4
           /
          3
        ```

        **Follow up:**

        - A solution using O(*n*) space is pretty straight forward.
        - Could you devise a constant space solution?

        Parameters
        ----------
        root: TreeNode

        Returns
        -------

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/recover-binary-search-tree/discuss/32559/Detail-Explain-about-How-Morris-Traversal-Finds-two-Incorrect-Pointer
        .. [2] https://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
        .. [3] https://leetcode.com/articles/recover-binary-search-tree/

        """
        x = y = pred = None

        def dfs(root):
            if not root:
                return
            nonlocal x, y, pred
            dfs(root.left)
            if pred and pred.val > root.val:
                y = root
                if x is None:
                    x = pred
                else:
                    return
            pred = root
            dfs(root.right)
        dfs(root)
        x.val, y.val = y.val, x.val

    def recoverTreeV01(self, root: TreeNode) -> None:
        x = y = pred = None
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right is not root:
                    prev = prev.right
                if prev.right is None:
                    prev.right = root
                    root = root.left
                else:
                    if pred and pred.val > root.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root
                    prev.right = None
                    root = root.right
            else:
                if pred and pred.val > root.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val


