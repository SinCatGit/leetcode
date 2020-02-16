
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    cnt = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/count-univalue-subtrees/

        Given a binary tree, count the number of uni-value subtrees.

        A Uni-value subtree means all nodes of the subtree have the same value.

        Example :

        Input:  root = {5,1,5,5,5,#,5}
        Output: 4
        Explanation:
                      5
                     / \
                    1   5
                   / |   |
                  5   5   5

        Input:  root = {1,3,2,4,5,#,6}
        Output: 3
        Explanation:
                      1
                     / \
                    3   2
                   / |   |
                  4   5   6


        References
        ---------
        .. [1] https://leetcode.com/articles/count-univalue-subtrees/
        .. [2] https://www.youtube.com/watch?v=gnSuBULGasw

        """
        self.is_valid_part(root, 0)
        return self.cnt

    def is_valid_part(self, node, val):
        if not node:
            return True
        if not all([self.is_valid_part(node.left, node.val), self.is_valid_part(node.right, node.val)]):
            return False
        self.cnt += 1
        return node.val == val

    def countUnivalSubtreesV01(self, root: TreeNode) -> int:

        if not root:
            return 0

        def traversal(r):
            if r.left is None and r.right is None:
                self.cnt += 1
                return r.val, True
            if r.left and r.right:
                lval, lbool = traversal(r.left)
                rval, rbool = traversal(r.right)
                if lbool and rbool and lval == r.val and rval == r.val:
                    self.cnt += 1
                    return r.val, True
            if not r.right:
                lval, lbool = traversal(r.left)
                if lbool and lval == r.val:
                    self.cnt += 1
                    return r.val, True
            if not r.left:
                rval, rbool = traversal(r.right)
                if rbool and rval == r.val:
                    self.cnt += 1
                    return r.val, True

            return r.val, False

        traversal(root)
        return self.cnt



