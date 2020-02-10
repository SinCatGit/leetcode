class Solution:
    def numberofDistinctIslands(self, grid):
        """
        https://leetcode.com/problems/number-of-distinct-islands/
        https://www.lintcode.com/problem/number-of-distinct-islands

        Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
        connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded
        by water.

        Count the number of distinct islands. An island is considered to be the same as another if and
        only if one island has the same shape as another island (and not rotated or reflected).

        Parameters
        ----------
        grid: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.numberofDistinctIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','0','1','1'],['0','0','0','1','1']])
        1
        >>> solution.numberofDistinctIslands([['1','1','0','0','1'],['1','0','0','0','0'],['1','1','0','0','1'],['0','1','0','1','1']])
        3

        Notes
        -----

        References
        ---------

        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        shapes = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    shapes.add(self.bfs(grid, i, j, rows, cols))
        return len(shapes)

    def bfs(self, grid, i, j, rows, cols):
        from collections import deque
        q = deque([(i, j)])
        shapes = set()
        delta_xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            grid[x][y] = '0'
            shapes.add((x-i, y-j))
            for dx, dy in delta_xy:
                _x, _y = x + dx, y + dy
                if 0 <= _x < rows and 0 <= _y <cols and grid[_x][_y] == '1':
                    q.append((_x, _y))
        return frozenset(shapes)





