from typing import List
from functools import lru_cache

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        """
        #### [1246. Palindrome Removal](https://leetcode.com/problems/palindrome-removal/)

        Given an integer array `arr`, in one move you can select a **palindromic** subarray `arr[i], arr[i+1], ..., arr[j]` where `i <= j`, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray  move to fill the gap left by the removal.

        Return the minimum number of moves needed to remove all numbers from the array.


        **Example 1:**

        ```
        Input: arr = [1,2]
        Output: 2
        ```

        **Example 2:**

        ```
        Input: arr = [1,3,4,1,5]
        Output: 3
        Explanation: Remove [4] then remove [1,3,1] then remove [5].
        ```

        **Constraints:**

        - `1 <= arr.length <= 100`
        - `1 <= arr[i] <= 20`


        Parameters
        ----------
        arr: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.minimumMoves([1, 3, 4, 1, 5])
        3

        References
        ---------
        .. [1] https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/
        """
        n = len(arr)
        dp = [[n for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif i+1 == j:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = min(dp[i+1][j-1] + (0 if arr[i] == arr[j] else 2), dp[i+1][j] + 1, dp[i][j-1]+1)
                    dp[i][j] = min(dp[i][j], min([dp[i][k]+dp[k+1][j] for k in range(i, j)]))
        return dp[0][-1]

    def minimumMovesV01(self, arr: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if i > j:
                return 0
            res = dp(i, j-1) + 1
            if arr[j] == arr[j-1]:
                res = min(res, dp(i, j-2)+1)
            for k in range(i, j-1):
                if arr[k] == arr[j]:
                    res = min(res, dp(i, k-1)+dp(k+1, j-1))
            return res
        return dp(0, len(arr)-1)





