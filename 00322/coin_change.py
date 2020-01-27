from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        https://leetcode.com/problems/coin-change/

        You are given coins of different denominations and a total amount of money amount.
        Write a function to compute the fewest number of coins that you need to make up that amount.
        If that amount of money cannot be made up by any combination of the coins, return -1.

        Parameters
        ----------
        coins: List[int]
        amount: int

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.coinChange([1, 2, 5], 11)
        3
        >>> solution.coinChange([2], 3)
        -1

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=htdBJul3xoc
        .. [2] https://www.youtube.com/watch?v=DJ4a7cmjZY0
        .. [3] https://www.youtube.com/watch?v=uUETHdijzkA

        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] < amount+1 else -1





