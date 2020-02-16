from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-postorder-traversal/

        Given a binary tree, return the postorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [3,2,1]
        Follow up: Recursive solution is trivial, could you do it iteratively?


        References
        ---------
        .. [1] https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization
        .. [2] https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45628/Morris-Traversal-Time-O(n)-Space-O(1)-inorder-preorder-postorder
        .. [3] https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45621/Preorder-Inorder-and-Postorder-Traversal-Iterative-Java-Solution

        """
        res = list()

        def post_order(r):
            if not r:
                return
            post_order(r.left)
            post_order(r.right)
            res.append(r.val)

        post_order(root)
        return res

    def postorderTraversalV01(self, root: TreeNode) -> List[int]:
        stack = list()
        res = list()
        while root or stack:
            if root:
                stack.append(root)
                res.insert(0, root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left

        return res


