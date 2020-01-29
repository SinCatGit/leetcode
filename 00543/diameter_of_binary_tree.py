
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/diameter-of-binary-tree/

        Given a binary tree, you need to compute the length of the diameter of the tree.
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        int

        Examples
        --------
        >>> node1=TreeNode(1)
        >>> node2=TreeNode(2)
        >>> node3=TreeNode(3)
        >>> node4=TreeNode(4)
        >>> node5=TreeNode(5)
        >>> node1.left=node2
        >>> node1.right=node3
        >>> node2.left=node4
        >>> node2.right=node5
        >>> solution = Solution()
        >>> solution.diameterOfBinaryTree(node1)
        3
        """
        def depth(r):
            if not r:
                return 0
            left = depth(r.left)
            right = depth(r.right)
            self.diameter = max(self.diameter, left+right)
            return max(left, right)+1

        depth(root)
        return self.diameter




