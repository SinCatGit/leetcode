

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        """
        https://leetcode.com/problems/path-sum-iii/

        You are given a binary tree in which each node contains an integer 
        value.

        Find the number of paths that sum to a given value.
        
        The path does not need to start or end at the root or a leaf, but it 
        must go downwards (traveling only from parent nodes to child nodes).
        
        The tree has no more than 1,000 nodes and the values are in the 
        range -1,000,000 to 1,000,000.
        
        Example:
        
        root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
        
              10
             /  \
            5   -3
           / |    \
          3   2   11
         / |   \
        3  -2   1
        
        Return 3. The paths that sum to 8 are:
        
        1.  5 -> 3
        2.  5 -> 2 -> 1
        3. -3 -> 11

        Parameters
        ----------
        root: TreeNode
        s: int

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/path-sum-iii/discuss/91878/17-ms-O(n)-java-Prefix-sum-method
        .. [2] https://leetcode.com/problems/path-sum-iii/discuss/91889/Simple-Java-DFS
        .. [3] https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

        """
        self.count = 0
        self.target = s

        def dfs(r, curr_sum, prefix_sum):
            if not r:
                return
            curr_sum += r.val
            if curr_sum-self.target in prefix_sum:
                self.count += prefix_sum[curr_sum-self.target]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            dfs(r.left, curr_sum, prefix_sum)
            dfs(r.right, curr_sum, prefix_sum)
            prefix_sum[curr_sum] -= 1

        dfs(root, 0, {0: 1})
        return self.count

    def pathSumV01(self, root: TreeNode, s: int) -> int:
        if not root:
            return 0
        return self.pathSumFrom(root, s) + self.pathSumV01(root.left, s) + self.pathSumV01(root.right, s)

    def pathSumFrom(self, root, s):
        if not root:
            return 0
        cnt = 0
        if root.val == s:
            cnt += 1

        return cnt + self.pathSumFrom(root.left, s-root.val) + self.pathSumFrom(root.right, s-root.val)
