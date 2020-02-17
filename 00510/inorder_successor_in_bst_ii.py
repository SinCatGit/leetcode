from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    is_find = False
    successor = None

    def inorderSuccessor(self, p: TreeNode) -> TreeNode:
        """
        https://leetcode.com/problems/inorder-successor-in-bst/

        Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

        The successor of a node p is the node with the smallest key greater than p.val.

        You will have direct access to the node but not to the root of the tree. Each node will
        have a reference to its parent node.

        Example 1:
        # Given the tree:
        #       2
        #      / \
        #     1   3

        Input: root = [2,1,3], p = 1
        Output: 2
        Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


        Example 2:
        # Given the tree:
        #         5
        #        / \
        #       3   6
        #      / \
        #     2   4
        #    /
        #   1
        Input: root = [5,3,6,2,4,null,null,1], p = 6
        Output: null
        Explanation: There is no in-order successor of the current node, so the answer is null.

        Note:

        If the given node has no in-order successor in the tree, return null.
        It's guaranteed that the values of the tree are unique.


        Parameters
        ----------
        p: TreeNode

        Returns
        -------
        TreeNode

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/inorder-successor-in-bst-ii/discuss/232213/Python-Iterative-O(logN)
        .. [2] https://www.programcreek.com/2013/02/leetcode-inorder-successor-in-bst-ii-java/
        .. [3] https://www.youtube.com/watch?v=5dySuyZf9Qg
        .. [4] https://www.youtube.com/watch?v=JdmAYw5h3G8

        """
        tmp = p.right
        while tmp and tmp.left:
            tmp = tmp.left
        if tmp:
            return tmp
        while p.parent:
            if p.parent.left == p:
                return p.parent
            p = p.parent


if __name__ == '__main__':
    sol = Solution()
    #          4
    #        /   \
    #       2     7
    #      / \   /
    #     1   3 5
    #            \
    #             6
    node4 = TreeNode(4)
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node4.left = node2
    node4.right = node7

    node2.parent = node4
    node7.parent = node4

    node2.left = node1
    node2.right = node3

    node1.parent = node2
    node3.parent = node2
    
    node7.left = node5

    node5.parent = node7
    node5.right = node6
    node6.parent = node5
    
    print(sol.inorderSuccessor(node6).val)







