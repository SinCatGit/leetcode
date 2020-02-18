class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/largest-bst-subtree/

        Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
        where largest means subtree with largest number of nodes in it.

        Note:
        A subtree must include all of its descendants.

        Example:

        Input: [10,5,15,1,8,null,7]

               10
               / \
             (5) 15
             / |   |
           (1) (8) 7

        Output: 3
        Explanation: The Largest BST Subtree in this case is the highlighted one.
                     The return value is the subtree's size, which is 3.
        Follow up:
        Can you figure out ways to solve it with O(n) time complexity?

        Hint:

        You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.


        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/largest-bst-subtree/discuss/78895/Short-Python-solution

        """
        def dfs(r):
            if not r:
                return 0, 0, float('inf'), float('-inf')
            largest_l, nl, min_l, max_l = dfs(r.left)
            largest_r, nr, min_r, max_r = dfs(r.right)
            n = nl + nr + 1 if max_l < r.val < min_r else float('-inf')
            return max(largest_l, largest_r, n), n, min(min_l, r.val), max(max_r, r.val)
        return dfs(root)[0]

    def largestBSTSubtreeV01(self, root: TreeNode) -> int:
        if not root:
            return 0
        if self.isValidBST(root):
            return self.count(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def count(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.count(root.left)
        right = self.count(root.right)
        return left + right + 1

    def isValidBST(self, root: TreeNode, down=float('-inf'), up=float('inf')) -> bool:
        if not root:
            return True
        return (down < root.val < up
                and self.isValidBST(root.left, down, root.val)
                and self.isValidBST(root.right, root.val, up))




