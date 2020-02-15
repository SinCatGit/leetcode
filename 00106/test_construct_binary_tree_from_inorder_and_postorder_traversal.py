import unittest
from construct_binary_tree_from_inorder_and_postorder_traversal import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root = sol.buildTree(
            [9, 3, 15, 20, 7],
            [9, 15, 7, 20, 3]
        )
        from collections import deque
        q = deque([root])
        lever_order = list()
        while q:
            node = q.popleft()
            lever_order.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        self.assertEqual([3, 9, 20, 15, 7], lever_order)


if __name__ == '__main__':
    unittest.main()
