import unittest
from next_greater_element_i import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([-1, 3, -1], sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
        self.assertEqual([3, -1], sol.nextGreaterElement([2, 4], [1, 2, 3, 4]))

        self.assertEqual([-1, 3, -1], sol.nextGreaterElementV01([4, 1, 2], [1, 3, 4, 2]))
        self.assertEqual([3, -1], sol.nextGreaterElementV01([2, 4], [1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
