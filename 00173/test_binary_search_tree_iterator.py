import unittest
from binary_search_tree_iterator import BSTIterator, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        #    5
        #   / \
        #   3  6
        #  /  \ \
        #  2  4  7

        node1 = TreeNode(5)
        node3 = TreeNode(3)
        node2 = TreeNode(6)
        node4 = TreeNode(2)
        node5 = TreeNode(4)
        node6 = TreeNode(7)

        node1.left = node3
        node1.right = node2
        node3.left = node4
        node3.right = node5
        node2.right = node6
        iterator = BSTIterator(node1)
        self.assertEqual(2, iterator.next())
        self.assertEqual(3, iterator.next())
        self.assertTrue(iterator.hasNext())

        self.assertEqual(4, iterator.next())
        self.assertTrue(iterator.hasNext())

        self.assertEqual(5, iterator.next())
        self.assertTrue(iterator.hasNext())

        self.assertEqual(6, iterator.next())
        self.assertTrue(iterator.hasNext())

        self.assertEqual(7, iterator.next())
        self.assertFalse(iterator.hasNext())


if __name__ == '__main__':
    unittest.main()
