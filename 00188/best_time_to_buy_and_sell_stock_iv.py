from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete at most two transactions.

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock
        before you buy again).

        Parameters
        ----------
        k: int
        prices: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.maxProfit(2, [2, 4, 1])
        2
        >>> solution.maxProfit(2, [2, 4, 1, 4, 3, 4])
        5
        >>> solution.maxProfit(4, [2, 4, 1, 4, 3, 4])
        6
        >>> solution.maxProfit(2, [3, 2, 6, 5, 0, 3])
        7
        >>> solution.maxProfit(2, [7, 6, 4, 3, 1])
        0

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=oDhu5uGq_ic

        """
        if not prices:
            return 0
        prices_len = len(prices)
        if k >= prices_len/2:
            max_profit = 0
            for i in range(1, prices_len):
                max_profit += max(0, prices[i]-prices[i-1])
            return max_profit

        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        pre, cur = 0, 1
        for i in range(1, k + 1):
            max_val = dp[pre][0] - prices[0]
            for j in range(1, len(prices)):
                max_val = max(max_val, dp[pre][j - 1] - prices[j - 1])
                dp[cur][j] = max(dp[cur][j - 1], max_val + prices[j])
            pre, cur = cur, pre
        return dp[pre][-1]
