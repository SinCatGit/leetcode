import unittest
from delete_node_in_a_bst import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
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

        from collections import deque
        q = deque([sol.deleteNode(node1, 0)])
        key_not_exist = []
        while q:
            node = q.popleft()
            key_not_exist.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        self.assertEqual([5, 3, 6, 2, 4, 7], key_not_exist)

        q = deque([sol.deleteNode(node1, 3)])
        key_exist = []
        while q:
            node = q.popleft()
            key_exist.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        self.assertEqual([5, 4, 6, 2, 7], key_exist)


if __name__ == '__main__':
    unittest.main()
