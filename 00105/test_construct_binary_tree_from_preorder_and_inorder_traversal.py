import unittest
from construct_binary_tree_from_preorder_and_inorder_traversal import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root = sol.buildTree(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7]
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

        root = sol.buildTreeV01(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7]
        )
        print(root.val)
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
