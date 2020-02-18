from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        https://leetcode.com/problems/maximum-binary-tree/

        Given an integer array with no duplicates. A maximum tree building on
        this array is defined as follow:

        The root is the maximum number in the array.
        The left subtree is the maximum tree constructed from left part subarray
        divided by the maximum number.
        The right subtree is the maximum tree constructed from right part subarray
        divided by the maximum number.
        Construct the maximum tree by the given array and output the root node of this tree.

        Example 1:
        Input: [3,2,1,6,0,5]
        Output: return the tree root node representing the following tree:

              6
            /   \
           3     5
            |    /
             2  0
               \
                1
        Note:
        The size of the given array will be in the range [1,1000].


        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        TreeNode

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/maximum-binary-tree/discuss/106156/Java-worst-case-O(N)-solution
        .. [2] https://leetcode.com/problems/maximum-binary-tree/discuss/106147/c-9-lines-on-log-n-map-plus-stack-with-binary-search
        .. [3] https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C++-O(N)-solution
        .. [4] https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.

        """
        if not nums:
            return None
        stack = list()
        for num in nums:
            current = TreeNode(num)
            while stack and stack[-1].val < num:
                current.left = stack.pop()
            if stack:
                stack[-1].right = current
            stack.append(current)
        return stack[0]

    def constructMaximumBinaryTreeV01(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None
        maxi = 0
        for i, v in enumerate(nums):
            if nums[maxi] < v:
                maxi = i

        left = self.constructMaximumBinaryTree(nums[:maxi])
        right = self.constructMaximumBinaryTree(nums[maxi+1:])

        node = TreeNode(nums[maxi])
        node.left = left
        node.right = right
        return node






