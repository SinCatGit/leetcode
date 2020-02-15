from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

        Given preorder and inorder traversal of a tree, construct the binary tree.

        Note:
        You may assume that duplicates do not exist in the tree.

        For example, given

        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        Return the following binary tree:

            3
           / \
          9  20
            /  \
           15   7

        Parameters
        ----------
        preorder: List[int]
        inorder: List[int]

        Returns
        -------
        TreeNode

        Examples
        --------

        Notes
        -----

        References
        ---------


        References
        ---------
        .. [1] https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map
        .. [2] https://medium.com/@shuangzizuobh2/how-well-do-you-code-python-9bec36bbc322
        .. [3] https://wiki.python.org/moin/TimeComplexity
        .. [4] https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.

        """
        from collections import deque
        preorder = deque(preorder)
        inorder = deque(inorder)

        def dfs(stop):
            if inorder and inorder[0] != stop:
                node = TreeNode(preorder.popleft())
                node.left = dfs(node.val)
                inorder.popleft()
                node.right = dfs(stop)
                return node

        return dfs(None)

    def buildTreeV01(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[ind])
            node.left = self.buildTreeV01(preorder, inorder[:ind])
            node.right = self.buildTreeV01(preorder, inorder[ind+1:])
            return node

