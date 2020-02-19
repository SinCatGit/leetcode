import unittest
from convert_binary_search_tree_to_sorted_doubly_linked_list import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #     2
        #    / \
        #   1   4
        #      / \
        #     3   6
        t25 = TreeNode(2)
        t21 = TreeNode(1)
        t24 = TreeNode(4)
        t23 = TreeNode(3)
        t26 = TreeNode(6)

        t25.left = t21
        t25.right = t24

        t24.left = t23
        t24.right = t26

        head = sol.treeToDoublyList(t25)

        def iterator(h):
            while h:
                yield h.val
                h = h.right

        i = iterator(head)

        self.assertEqual(1, next(i))
        self.assertEqual(2, next(i))
        self.assertEqual(3, next(i))
        self.assertEqual(4, next(i))
        self.assertEqual(6, next(i))

        self.assertEqual(1, next(i))
        self.assertEqual(2, next(i))
        self.assertEqual(3, next(i))
        self.assertEqual(4, next(i))
        self.assertEqual(6, next(i))


if __name__ == '__main__':
    unittest.main()
