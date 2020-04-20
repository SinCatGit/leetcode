from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """


        Parameters
        ----------
        n: int

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/number-of-digit-one/discuss/64381/4%2B-lines-O(log-n)-C%2B%2BJavaPython

        """
        if not matrix or not matrix[0]:
            return 0
        from collections import defaultdict, deque
        edges = defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        degrees = {(x, y): 0 for x in range(m) for y in range(n)}

        dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                for dx, dy in dxy:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        edges[(i, j)].append((x, y))
                        degrees[(x, y)] += 1
        result = 0
        queue = deque([k for k, v in degrees.items() if v == 0])
        while queue:
            size = len(queue)
            for i in range(size):
                res = queue.popleft()
                for item in edges[res]:
                    degrees[item] -= 1
                    if degrees[item] == 0:
                        queue.append(item)
            result += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    m = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
        [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
        [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
        [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
        [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
        [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
        [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
        [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
        [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
        [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(sol.longestIncreasingPath(m))

