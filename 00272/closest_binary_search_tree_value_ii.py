from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0
    min_val = float('inf')

    def closestValue(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        https://leetcode.com/problems/closest-binary-search-tree-value/

        Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.


        Note:

        Given target value is a floating point.
        You may assume k is always valid, that is: k ≤ total nodes.
        You are guaranteed to have only one unique set of k values in the BST that are closest to the target.


        Parameters
        ----------
        root: TreeNode
        target: float
        k: int

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70327/4-7-lines-recursiveiterative-RubyC%2B%2BJavaPython

        """
        res = list()
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if len(res) >= k:
                    if abs(res[0] - target) > abs(root.val-target):
                        res.pop(0)
                        res.append(root.val)
                    else:
                        break
                else:
                    res.append(root.val)
                root = root.right
        return res


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
    
    print(sol.closestValue(node4, 9, 3))







