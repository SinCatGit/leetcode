class Solution:
    def wallsAndGates(self, rooms):
        """
        https://leetcode.com/problems/walls-and-gates/

        You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume
        that the distance to a gate is less than 2147483647.

        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate,
        that room should remain filled with INF

        Parameters
        ----------
        rooms: List[List[int]]

        Returns
        -------
        None

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        if not rooms or not rooms[0]:
            return
        rows, cols = len(rooms), len(rooms[0])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, rows, cols, 0)

    def dfs(self, rooms, x, y, rows, cols, depth):
        if rooms[x][y] == -1:
            return

        if rooms[x][y] < depth:
            return

        rooms[x][y] = depth
        delta_xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in delta_xy:
            _x, _y = dx+x, dy+y
            if 0 <= _x < rows and 0 <= _y < cols:
                self.dfs(rooms, _x, _y, rows, cols, depth+1)


if __name__ == '__main__':
    solution = Solution()
    r = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    solution.wallsAndGates(r)


