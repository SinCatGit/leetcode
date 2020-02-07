from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        https://leetcode.com/problems/continuous-subarray-sum/

        Given a list of non-negative numbers and a target integer k, write a function to check if the array has
        a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k
        where n is also an integer.

        Parameters
        ----------
        nums: List[int]
        k: int

        Returns
        -------
        bool

        Examples
        --------
        >>> solution = Solution()
        >>> solution.checkSubarraySum([23, 2, 4, 6, 7], 6)
        True
        >>> solution.checkSubarraySum([4, 6, 7], 6)
        False
        >>> solution.checkSubarraySum([0, 0, 4, 6, 7], 0)
        True
        >>> solution.checkSubarraySum([0, 1, 0], 0)
        False

        Notes
        -----

        References
        ---------

        """
        if k < 0:
            k *= -1

        from collections import defaultdict
        sub_hash = defaultdict(list)
        sub_hash[0].append(-1)
        prefix_sum = 0
        for i, n in enumerate(nums):
            prefix_sum += n
            key = prefix_sum if k == 0 else prefix_sum % k
            for j in sub_hash[key]:
                if i > j + 1:
                    return True
            sub_hash[key].append(i)
        return False
