from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    is_find = False
    successor = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        https://leetcode.com/problems/inorder-successor-in-bst/

        Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

        The successor of a node p is the node with the smallest key greater than p.val.

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
        root: TreeNode
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
        .. [1] https://www.cnblogs.com/grandyang/p/5306162.html

        """
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res

    def inorderSuccessorV02(self, root: TreeNode, p: TreeNode) -> TreeNode:

        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val == p.val:
                    self.is_find = True
                elif self.is_find and not self.successor:
                    self.successor = root
                    break
                root = root.right
        return self.successor

    def inorderSuccessorV01(self, root: TreeNode, p: TreeNode) -> TreeNode:

        def dfs(r):
            if not r:
                return
            dfs(r.left)
            if r.val == p.val:
                self.is_find = True
            elif self.is_find and not self.successor:
                self.successor = r
            dfs(r.right)
        dfs(root)
        return self.successor


if __name__ == '__main__':
    sol = Solution()
    #          4
    #        /   \
    #       2     7
    #      / \   /
    #     1   3 5
    node4 = TreeNode(4)
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node7 = TreeNode(7)

    node4.left = node2
    node4.right = node7

    node2.left = node1
    node2.right = node3
    
    node7.left = node5
    
    print(sol.inorderSuccessor(node4, node5).val)







