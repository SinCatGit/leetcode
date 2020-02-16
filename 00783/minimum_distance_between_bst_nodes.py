
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = float('inf')
    pre = float('-inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/minimum-distance-between-bst-nodes/

        Given a Binary Search Tree (BST) with the root node root, return the minimum
        difference between the values of any two different nodes in the tree.

        Example :

        Input: root = [4,2,6,1,3,null,null]
        Output: 1
        Explanation:
        Note that root is a TreeNode object, not an array.

        The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

                  4
                /   \
              2      6
             / \
            1   3

        while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
        Note:

        The size of the BST will be between 2 and 100.
        The BST is always valid, each node's value is an integer, and each node's value is different.


        References
        ---------
        .. [1] https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/114834/C%2B%2BJavaPython-Inorder-Traversal-O(N)-time-Recursion
        .. [2] https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/238404/100-Python-Solution-%2B-Detailed-Explanation

        """
        def traversal(r):
            if not r:
                return
            traversal(r.left)
            self.res = min(self.res, r.val-self.pre)
            self.pre = r.val
            traversal(r.right)

        traversal(root)
        return int(self.res)



