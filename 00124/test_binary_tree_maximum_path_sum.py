import unittest
from binary_tree_maximum_path_sum import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node1.left = node2
        node1.right = node3

        node_10 = TreeNode(-10)
        node9 = TreeNode(9)
        node20 = TreeNode(20)
        node_10.left = node9
        node_10.right = node20
        node15 = TreeNode(15)
        node7 = TreeNode(7)
        node20.left = node15
        node20.right = node7

        cnode1 = TreeNode(5)
        cnode2 = TreeNode(4)
        cnode3 = TreeNode(8)
        cnode1.left = cnode2
        cnode1.right = cnode3

        cnode4 = TreeNode(11)
        cnode6 = TreeNode(13)
        cnode7 = TreeNode(4)

        cnode2.left = cnode4
        cnode3.left = cnode6
        cnode3.right = cnode7

        cnode8 = TreeNode(7)
        cnode9 = TreeNode(2)
        cnode14 = TreeNode(1)

        cnode4.left = cnode8
        cnode4.right = cnode9
        cnode7.left = cnode14

        solution = Solution()
        self.assertEqual(6, solution.maxPathSum(node1))
        self.assertEqual(42, solution.maxPathSum(node_10))
        self.assertEqual(48, solution.maxPathSum(cnode1))


if __name__ == '__main__':
    unittest.main()
