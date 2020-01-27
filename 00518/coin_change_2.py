from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        https://leetcode.com/problems/coin-change-2/

        You are given coins of different denominations and a total amount of money.
        Write a function to compute the number of combinations that make up that amount.
        You may assume that you have infinite number of each kind of coin.

        Parameters
        ----------
        amount: int
        coins: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.change(5, [1, 2, 5])
        4
        >>> solution.change(3, [2])
        0
        >>> solution.change(10, [10])
        1

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=ZKAILBWl08g&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m
        .. [1] https://www.youtube.com/watch?v=DJ4a7cmjZY0
        """
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


