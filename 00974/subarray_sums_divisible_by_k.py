from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        https://leetcode.com/problems/subarray-sums-divisible-by-k/

        Given an array A of integers, return the number of (contiguous, non-empty) subarrays
        that have a sum divisible by K.

        Parameters
        ----------
        A: List[int]
        K: int

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
        7

        Notes
        -----

        References
        ---------

        """
        prefix_sum = 0
        sub_hash = {0: 1}
        cnt = 0
        for n in A:
            prefix_sum += n
            cnt += sub_hash.get(prefix_sum % K, 0)
            sub_hash[prefix_sum % K] = sub_hash.get(prefix_sum % K, 0) + 1
        return cnt

