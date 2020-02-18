from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        """
        https://leetcode.com/problems/two-sum-less-than-k/

        Given an array A of integers and integer K, return the maximum S such that
        there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

        Example 1:

        Input: A = [34,23,1,24,75,33,54,8], K = 60
        Output: 58
        Explanation:
        We can use 34 and 24 to sum 58 which is less than 60.
        Example 2:

        Input: A = [10,20,30], K = 15
        Output: -1
        Explanation:
        In this case it's not possible to get a pair sum less that 15.
        Note:

        1 <= A.length <= 100
        1 <= A[i] <= 1000
        1 <= K <= 2000

        Parameters
        ----------
        A: List[int]
        K: int

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://www.cnblogs.com/Dylan-Java-NYC/p/11368115.html
        .. [2] https://leetcode.com/problems/two-sum-less-than-k/discuss/323522/Python-simple-solution

        """
        A.sort()
        i, j = 0, len(A)-1
        ans = -1
        while i < j:
            if A[i] + A[j] < K:
                ans = max(ans, A[i] + A[j])
                i += 1
            else:
                j -= 1

        return ans













