class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    successor = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        https://leetcode.com/problems/convert-bst-to-greater-tree/

        Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key
        of the original BST is changed to the original key plus sum of all keys greater
        than the original key in BST.

        Example:

        Input: The root of a Binary Search Tree like this:
                      5
                    /   \
                   2     13

        Output: The root of a Greater Tree like this:
                     18
                    /   \
                  20     13

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        TreeNode

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/largest-bst-subtree/discuss/78895/Short-Python-solution

        """
        stack = list()
        res = root
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                self.successor += root.val
                root.val = self.successor
                root = root.left
        return res





