from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-preorder-traversal/

        Given a binary tree, return the preorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [1,2,3]
        Follow up: Recursive solution is trivial, could you do it iteratively?


        References
        ---------
        .. [1] https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45273/Very-simple-iterative-Python-solution

        """
        res = list()

        def pre_order(r):
            if not r:
                return
            res.append(r.val)
            pre_order(r.left)
            pre_order(r.right)

        pre_order(root)
        return res

    def preorderTraversalV01(self, root: TreeNode) -> List[int]:
        stack = list()
        res = list()

        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right

        return res


