from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete at most two transactions.

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock
        before you buy again).

        Parameters
        ----------
        prices: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
        6
        >>> solution.maxProfit([1, 2, 3, 4, 5])
        4
        >>> solution.maxProfit([7, 6, 4, 3, 1])
        0

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=oDhu5uGq_ic

        """
        k = 2
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            max_val = dp[i-1][0]-prices[0]
            for j in range(1, len(prices)):
                max_val = max(max_val, dp[i-1][j-1]-prices[j-1])
                dp[i][j] = max(dp[i][j-1], max_val+prices[j])
        return dp[-1][-1]

    def maxProfitV01(self, prices:List[int]) -> int:
        k = 2
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            for j in range(1, len(prices)):
                max_val = max([dp[i-1][m]+prices[j]-prices[m] for m in range(j)])
                dp[i][j] = max(dp[i][j-1], max_val)
        return dp[-1][-1]
