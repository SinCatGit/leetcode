import unittest
from construct_binary_tree_from_string import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root = sol.str2tree('-4(-20(31)(1))(6(5))')
        from collections import deque
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        self.assertEqual([-4, -20, 6, 31, 1, 5], res)


if __name__ == '__main__':
    unittest.main()
