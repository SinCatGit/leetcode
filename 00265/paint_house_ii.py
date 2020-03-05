from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        [265. Paint House II](https://leetcode.com/problems/paint-house-ii/)

        There are a row of n houses, each house can be painted with one of the k colors.
        The cost of painting each house with a certain color is different. You have to paint
        all the houses such that no two adjacent houses have the same color.

        The cost of painting each house with a certain color is represented by a n x k cost
        matrix. For example, costs[0][0] is the cost of painting house 0 with color 0;
        costs[1][2]is the cost of painting house 1 with color 2, and so on...
        Find the minimum cost to paint all houses.

        **Note:**

        All costs are positive integers.

        **Example 1**
        ```
        Input:
        costs = [[14,2,11],[11,14,5],[14,3,10]]
        Output: 10
        Explanation:
        The three house use color [1,2,1] for each house. The total cost is 10.
        ```

        **Example 2**
        ```
        Input:
        costs = [[5]]
        Output: 5
        Explanation:
        There is only one color and one house.
        ```

        **Follow up:**

        Could you solve it in O(nk) runtime?

        """
        if not costs or not costs[0]:
            return 0
        m, n = len(costs), len(costs[0])
        idx = -1
        min1, min2 = 0, 0
        for i in range(m):
            last1, last2 = min1, min2
            min1, min2 = float('inf'), float('inf')
            last_idx = idx
            for j in range(n):
                t = costs[i][j] + (last1 if last_idx != j else last2)
                if t < min1:
                    min2, idx, min1 = min1, j, t
                elif t < min2:
                    min2 = t
        return min1

    def minCostIIV03(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        m, n = len(costs), len(costs[0])
        min1, min2 = -1, -1
        dp = [0 for _ in range(n)]
        for i in range(m):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            prev = dp[:]
            for j in range(n):
                if j != last1:
                    dp[j] = costs[i][j] + (prev[last1] if last1 >= 0 else 0)
                else:
                    dp[j] = costs[i][j] + (prev[last2] if last2 >= 0 else 0)

                if min1 == -1 or dp[j] < dp[min1]:
                    min2 = min1
                    min1 = j
                elif min2 == -1 or dp[j] < dp[min2]:
                    min2 = j
        return dp[min1]

    def minCostIIV02(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        m = len(costs)
        n = len(costs[0])
        dp = [i for i in costs[0]]
        for i in range(1, m):
            prev = dp[:]
            for j in range(n):
                dp[j] = costs[i][j] + min(prev[:j]+prev[j+1:])
        return min(dp)

    def minCostIIV01(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        m = len(costs)
        n = len(costs[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = costs[0]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = costs[i][j] + min(dp[i-1][:j]+dp[i-1][j+1:])
        return min(dp[-1])

