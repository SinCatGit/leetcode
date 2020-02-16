
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def splitBST(self, root: TreeNode, val: int) -> (TreeNode, TreeNode):
        """
        https://leetcode.com/problems/split-bst/

        Given a Binary Search Tree (BST) with root node root, and a target value V,
        split the tree into two subtrees where one subtree has nodes that are all
        smaller or equal to the target value, while the other subtree has all nodes
        that are greater than the target value.  It's not necessarily the case that
        the tree contains a node with value V.

        Additionally, most of the structure of the original tree should remain.  Formally,
        for any child C with parent P in the original tree, if they are both in the same
        subtree after the split, then node C should still have the parent P.

        You should output the root TreeNode of both subtrees after splitting, in any order.

        Example 1:

        Input: root = [4,2,6,1,3,5,7], V = 2
        Output: [[2,1],[4,3,6,null,null,5,7]]
        Explanation:
        Note that root, output[0], and output[1] are TreeNode objects, not arrays.

        The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

                  4
                /   \
              2      6
             / |    / \
            1  3  5   7

        while the diagrams for the outputs are:

                  4
                /   \
              3      6      and    2
                    / |           /
                   5   7         1
        Note:

        The size of the BST will not exceed 50.
        The BST is always valid and each node's value is different.


        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/8993143.html
        .. [2] https://leetcode.com/problems/split-bst/discuss/159985/Python-DFS-tm
        .. [3] https://leetcode.com/problems/split-bst/discuss/113799/Python-straightforward-recursive-solution

        """
        if not root:
            return None, None
        if root.val <= val:
            lt, gt = self.splitBST(root.right, val)
            lt, root.right = root, lt
        else:
            lt, gt = self.splitBST(root.left, val)
            gt, root.left = root, gt
        return lt, gt


if __name__ == '__main__':
    sol = Solution()

    #
    #      4
    #     /  \
    #   2     6
    #  / \   / \
    # 1   3 5   7

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node4.left = node2
    node4.right = node6
    node2.left = node1
    node2.right = node3
    node6.left = node5
    node6.right = node7

    little, greater = sol.splitBST(node4, 2)

    def dfs(r):
        if r.left:
            yield from dfs(r.left)
        yield r.val
        if r.right:
            yield from dfs(r.right)

    for i, v in enumerate(dfs(little)):
        print(i, v)
    for i, v in enumerate(dfs(greater)):
        print(i, v)



