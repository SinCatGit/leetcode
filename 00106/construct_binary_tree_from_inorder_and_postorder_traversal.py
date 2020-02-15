from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

        Given inorder and postorder traversal of a tree, construct the binary tree.

        Note:
        You may assume that duplicates do not exist in the tree.

        For example, given

        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        Return the following binary tree:

            3
           / \
          9  20
            /  \
           15   7

        Parameters
        ----------
        inorder: List[int]
        postorder: List[int]

        Returns
        -------
        TreeNode

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.

        """
        if inorder:
            ind = inorder.index(postorder[-1])
            node = TreeNode(inorder[ind])
            node.left = self.buildTree(inorder[:ind], postorder[:ind])
            node.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
            return node

