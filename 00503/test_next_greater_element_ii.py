import unittest
from next_greater_element_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([3, 4, -1, 3], sol.nextGreaterElements([1, 3, 4, 2]))
        self.assertEqual(
            [2, 3, 4, 5, 6, -1, 6, 5, 6, 2, 3, 4],
            sol.nextGreaterElements([1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3])
        )


if __name__ == '__main__':
    unittest.main()
