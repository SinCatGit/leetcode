import unittest
from copy_list_with_random_pointer import Solution, Node


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        node7 = Node(7)
        node13 = Node(13)
        node11 = Node(11)
        node10 = Node(10)
        node1 = Node(1)

        node7.next = node13

        node13.next = node11
        node13.random = node7

        node11.next = node10
        node11.random = node1

        node10.next = node1
        node10.random = node11

        node1.random = node7

        new_head = sol.copyRandomList(node7)
        head = node7

        while new_head:
            self.assertEqual(head.val, new_head.val)
            if new_head.random:
                self.assertEqual(head.random.val, new_head.random.val)
            head = head.next
            new_head = new_head.next

        new_head = sol.copyRandomListV01(node7)
        head = node7

        while new_head:
            self.assertEqual(head.val, new_head.val)
            if new_head.random:
                self.assertEqual(head.random.val, new_head.random.val)
            head = head.next
            new_head = new_head.next

        new_head = sol.copyRandomListV02(node7)
        head = node7

        while new_head:
            self.assertEqual(head.val, new_head.val)
            if new_head.random:
                self.assertEqual(head.random.val, new_head.random.val)
            head = head.next
            new_head = new_head.next


if __name__ == '__main__':
    unittest.main()
