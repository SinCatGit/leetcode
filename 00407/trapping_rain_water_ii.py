from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        [407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

        Given an m x n matrix of positive integers representing the height of each unit cell in a 2D
        elevation map, compute the volume of water it is able to trap after raining.

        **Note:**

        Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

        **Example:**
        ```
        Given the following 3x6 height map:
        [
          [1,4,3,1,3,2],
          [3,2,1,3,2,4],
          [2,3,3,2,3,1]
        ]

        Return 4.
        ```

        The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

        After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

        Parameters
        ----------
        heightMap: List[List[int]]

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4],[2, 3, 3, 2, 3, 1]]
        4

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
        .. [2] https://leetcode.com/problems/trapping-rain-water-ii/discuss/142829/Python-concise-and-readable-solution
        .. [3] https://www.youtube.com/watch?v=cJayBq38VYw&feature=emb_logo
        .. [4] https://www.youtube.com/watch?v=ZEgoEf8HGKI

        """
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])

        hp = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            hp.append((heightMap[i][0], i, 0))
            visited[i][0] = True
            hp.append((heightMap[i][n-1], i, n-1))
            visited[i][n-1] = True

        for j in range(n):
            hp.append((heightMap[0][j], 0, j))
            visited[0][j] = True
            hp.append((heightMap[m-1][j], m-1, j))
            visited[m-1][j] = True

        heapify(hp)
        dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = 0
        while hp:
            h, r, c = heappop(hp)
            for dx, dy in dxy:
                x = r + dx
                y = c + dy
                if 0 < x < m-1 and 0 < y < n-1 and not visited[x][y]:
                    heappush(hp, (max(heightMap[x][y], h), x, y))
                    visited[x][y] = True
                    ans += max(h-heightMap[x][y], 0)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.trapRainWater([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]))

    print(sol.trapRainWater([
        [12, 13, 1, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13]
    ]))

