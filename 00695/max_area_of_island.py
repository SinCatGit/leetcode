from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/max-area-of-island/

        Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
        connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded
        by water.

        Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

        Parameters
        ----------
        grid: List[List[int]]

        Returns
        -------
        List

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = max(area, self.bfs(grid, i, j, rows, cols))
        return area

    def bfs(self, grid, x, y, rows, cols):
        from collections import deque
        q = deque([(x, y)])
        delta_xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        area = 0
        grid[x][y] = 0
        while q:
            area += 1
            x, y = q.popleft()

            for dx, dy in delta_xy:
                _x, _y = x + dx, y + dy
                if 0 <= _x < rows and 0 <= _y < cols and grid[_x][_y] == 1:
                    grid[_x][_y] = 0
                    q.append((_x, _y))
        return area

