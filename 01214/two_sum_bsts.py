from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """
        https://leetcode.com/problems/two-sum-bsts/

        Given two binary search trees, return True if and only if there is a node in the first tree
        and a node in the second tree whose values sum up to a given integer target.


        Example:
             2     1
            / |   / |
           1  4  0  3

        Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
        Output: true
        Explanation: 2 and 3 sum up to 5.

        Parameters
        ----------
        root1: TreeNode
        root2: TreeNode
        target: int

        Returns
        -------
        bool

        Examples
        --------

        References
        ---------
        .. [1] https://www.acwing.com/solution/LeetCode/content/5097/
        .. [2] https://www.zhangjc.site/5080-two-sum-bsts/

        """
        stack1 = list()
        visit = set()
        while root1 or stack1:
            if root1:
                stack1.append(root1)
                root1 = root1.left
            else:
                root1 = stack1.pop()
                visit.add(root1.val)
                root1 = root1.right
        stack2 = list()
        while root2 or stack2:
            if root2:
                stack2.append(root2)
                root2 = root2.left
            else:
                root2 = stack2.pop()
                if target - root2.val in visit:
                    return True
                root2 = root2.right
        return False













