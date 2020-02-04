from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions
        as you like (i.e., buy one and sell one share of the stock multiple times).

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
        >>> solution.maxProfit([7, 1, 5, 3, 6, 4])
        7
        >>> solution.maxProfit([1, 2, 3, 4, 5])
        4
        >>> solution.maxProfit([7, 6, 4, 3, 1])
        0

        Notes
        -----

        References
        ---------

        """
        return sum([max(0, prices[i]-prices[i-1]) for i in range(1, len(prices))])

    def maxProfitV01(self, prices: List[int]) -> int:
        i, profit, prices_len = 0, 0, len(prices)
        while i < prices_len:
            while i < prices_len - 1 and prices[i] > prices[i+1]:
                i += 1
            min_val = prices[i]
            i += 1
            while i < prices_len - 1 and prices[i] <= prices[i+1]:
                i += 1
            if i < prices_len:
                profit += prices[i] - min_val
        return profit
