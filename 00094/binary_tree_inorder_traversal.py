from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/

        Given a binary tree, return the inorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [1,3,2]
        Follow up: Recursive solution is trivial, could you do it iteratively?


        References
        ---------
        .. [1] https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31467/Morris-Traversal-NO-RECURSION-NO-STACK
        .. [2] https://codeoverflow.wordpress.com/tag/morris-inorder-traversal/
        .. [3] https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions.

        """
        res = list()

        def in_order(r):
            if not r:
                return
            in_order(r.left)
            res.append(r.val)
            in_order(r.right)
        in_order(root)
        return res

    def inorderTraversalV01(self, root: TreeNode) -> List[int]:
        stack = list()
        res = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversalV02(self, root: TreeNode) -> List[int]:
        stack = list()
        res = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

