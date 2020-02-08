from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        https://leetcode.com/problems/surrounded-regions/

        Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

        A region is captured by flipping all 'O's into 'X's in that surrounded region.

        Do not return anything, modify board in-place instead.

        Parameters
        ----------
        board: List[List[str]]

        Returns
        -------
        None

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=kyvGkcXs_rE

        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            self.dfs(board, i, 0, rows, cols)
            self.dfs(board, i, cols-1, rows, cols)

        for j in range(cols):
            self.dfs(board, 0, j, rows, cols)
            self.dfs(board, rows-1, j, rows, cols)
        replace_map = {
            '@': 'O',
            'X': 'X',
            'O': 'X'
        }
        for i in range(rows):
            for j in range(cols):
                board[i][j] = replace_map[board[i][j]]

    def dfs(self, board, x, y, rows, cols):
        if board[x][y] != 'O':
            return
        board[x][y] = '@'
        delta_xy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in delta_xy:
            _x, _y = x + dx, y + dy
            if 0 <= _x < rows and 0 <= _y < cols:
                self.dfs(board, _x, _y, rows, cols)


if __name__ == '__main__':
    solution = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution.solve(board)

