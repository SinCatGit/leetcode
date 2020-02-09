
class Solution():
    def numIslands(self, grid) -> int:
        """
        https://leetcode.com/problems/number-of-islands/

        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded
        by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges
        of the grid are all surrounded by water.

        Parameters
        ----------
        grid: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])
        3

        Notes
        -----

        References
        ---------

        """
        if not grid or not grid[0] or not grid[0][0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j, rows, cols)
        return cnt

    def dfs(self, grid, x, y, rows, cols):
        if grid[x][y] == '0':
            return

        dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        grid[x][y] = '0'
        for dx, dy in dxdy:
            _x, _y = x+dx, y+dy
            if 0 <= _x < rows and 0 <= _y < cols:
                self.dfs(grid, _x, _y, rows, cols)

    def numIslandsV01(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def sink(x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                grid[x][y] = '0'
                list(map(sink, (x, x, x+1, x-1), (y+1, y-1, y, y)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(rows) for j in range(cols))





