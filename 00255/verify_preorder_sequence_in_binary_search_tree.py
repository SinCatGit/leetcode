from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    successor = 0

    def verifyPreorder(self, preorder: List[int]) -> bool:

        """
        https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

        Given an array of numbers, verify whether it is the correct preorder traversal
        sequence of a binary search tree.

        You may assume each number in the sequence is unique.

        Consider the following binary search tree:

             5
            / \
           2   6
          / \
         1   3
        Example 1:

        Input: [5,2,6,1,3]
        Output: false
        Example 2:

        Input: [5,2,1,3,6]
        Output: true
        Follow up:
        Could you do it using only constant space complexity?

        Parameters
        ----------
        preorder: List[int]

        Returns
        -------
        bool

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/68142/Java-O(n)-and-O(1)-extra-space
        .. [2] https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/255712/JavaC%2B%2BPython-O(N)-Recursion

        """
        preorder_len = len(preorder)
        low = float('-inf')
        i = -1

        for j in range(preorder_len):
            if preorder[j] < low:
                return False

            while i >= 0 and preorder[j] > preorder[i]:
                low = preorder[i]
                i -= 1
                
            i += 1
            preorder[i] = preorder[j]
        return True

    def verifyPreorderV02(self, preorder: List[int]) -> bool:

        low = float('-inf')
        stack = list()

        for p in preorder:
            if p < low:
                return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        return True

    def verifyPreorderV01(self, preorder: List[int]) -> bool:

        if not preorder:
            return True
        val = preorder[0]
        i, j = 1, 1

        while i < len(preorder) and preorder[i] < val:
            i += 1
        j = i
        while i < len(preorder) and preorder[i] > val:
            i += 1
        if i != len(preorder):
            return False
        return self.verifyPreorder(preorder[1:j]) and self.verifyPreorder(preorder[j:])






