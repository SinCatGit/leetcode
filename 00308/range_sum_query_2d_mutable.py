from typing import List


class NumMatrix(object):
    """
    [308. Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable)

    Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

    Range Sum Query 2D
    The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

    **Example:**

    ```
    Given matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    update(3, 2, 2)
    sumRegion(2, 1, 4, 3) -> 10
    ```

    **Note:**

    - The matrix is only modifiable by the update function.
    - You may assume the number of calls to update and sumRegion function is distributed evenly.
    - You may assume that row1 ≤ row2 and col1 ≤ col2.

    References
    ----------
    .. [1] https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75870/java-2d-binary-indexed-tree-solution-clean-and-short-17ms
    .. [2] https://www.youtube.com/watch?v=CWDQJGaN1gY
    .. [3] https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/

    """

    def __init__(self, matrix: List[List[int]]):
        """
        :type matrix: List[List[int]]
        """
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0]*self.n for _ in range(self.m)]
        self.bit = [[0]*(self.n+1) for _ in range(self.m+1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i < self.m+1:
            j = col + 1
            while j < self.n+1:
                self.bit[i][j] += diff
                j += j & -j
            i += i & -i

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        res += self.range_sum(row2, col2)
        res += self.range_sum(row1 - 1, col1 - 1)
        res -= self.range_sum(row2, col1 - 1)
        res -= self.range_sum(row1 - 1, col2)
        return res

    def range_sum(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)

        return res


class NumMatrixV01(object):
    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.d = matrix
        for row in self.d:
            for j in range(1, self.n):
                row[j] += row[j-1]

    def update(self, row, col, val):
        row = self.d[row]
        orig = row[col] - (row[col-1] if col else 0)
        diff = val - orig
        for j in range(col, self.n):
            row[j] += diff

    def sumRegion(self, row1, col1, row2, col2):
        res = 0
        for r in range(row1, row2+1):
            res += self.d[r][col2] - (self.d[r][col1-1] if col1 else 0)
        return res


