from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate-iii/

        Given an array of integers, find out whether there are two distinct indices
        i and j in the array such that the absolute difference between nums[i] and nums[j]
        is at most t and the absolute difference between i and j is at most k.

        Parameters
        ----------
        nums: List[int]
        k: int
        t: int

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
        True
        >>> sol.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
        True
        >>> sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
        False

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=yc4hCFzNNQc
        .. [2] https://leetcode-cn.com/problems/contains-duplicate-iii/solution/cun-zai-zhong-fu-yuan-su-iii-by-leetcode/
        .. [3] https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets

        """
        if k <= 0 or t < 0:
            return False
        bucket = {}
        w = t + 1
        min_val, max_val = min(nums), max(nums)
        for i, n in enumerate(nums):
            m = (n - min_val) // w
            if m in bucket:
                return True
            if m + 1 in bucket and abs(bucket[m+1] - n) <= t:
                return True
            if m - 1 in bucket and abs(bucket[m-1] - n) <= t:
                return True
            bucket[m] = n
            if i >= k:
                bucket.pop((nums[i-k]-min_val)//w)
        return False

    def containsNearbyAlmostDuplicateV01(self, nums: List[int], k: int, t: int) -> bool:
        nums_len = len(nums)
        for i, n in enumerate(nums):
            j = i + 1
            while j < nums_len and j - i <= k:
                if abs(nums[j] - n) <= t:
                    return True
                j += 1
        return False



