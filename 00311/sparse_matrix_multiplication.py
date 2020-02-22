from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/sparse-matrix-multiplication

        Given two sparse matrices A and B, return the result of AB.

        You may assume that A's column number is equal to B's row number.

        Example:

        A = [
          [ 1, 0, 0],
          [-1, 0, 3]
        ]

        B = [
          [ 7, 0, 0 ],
          [ 0, 0, 0 ],
          [ 0, 0, 1 ]
        ]


             |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
        AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                          | 0 0 1 |

        Parameters
        ----------
        A: List[List[int]]
        B: List[List[int]]

        Returns
        -------
        List[List[int]]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
        [[7, 0, 0], [-7, 0, 3]]

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/5282959.html
        .. [2] https://leetcode.com/problems/sparse-matrix-multiplication/discuss/76178/Short-Python-solution

        """
        cols = [[(v, j) for j, v in enumerate(col) if v] for col in zip(*B)]

        return [[sum(row[j]*v for v, j in col) for col in cols] for row in A]
