from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

        Given a *m* x *n* matrix, if an element is 0, set its entire row and column to 0. Do
        it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).

        **Example 1:**

        ```
        Input:
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        Output:
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]
        ```

        **Example 2:**

        ```
        Input:
        [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
        ]
        Output:
        [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]
        ```

        **Follow up:**

        - A straight forward solution using O(*m**n*) space is probably a bad idea.
        - A simple improvement uses O(*m* + *n*) space, but still not the best solution.
        - Could you devise a constant space solution?

        Parameters
        ----------
        matrix: List[List[int]]

        Returns
        -------
        None

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/set-matrix-zeroes/discuss/26115/JavaPython-O(1)-space-11-lines-solution

        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        is_first_zero = not all(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, m):
            for j in range(n)[::-1]:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if is_first_zero:
            matrix[0] = [0] * n
