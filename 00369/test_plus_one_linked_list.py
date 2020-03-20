import unittest
from plus_one_linked_list import Solution, ListNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):

        def iter_list(head):
            res = []
            while head:
                res.append(head.val)
                head = head.next
            return res

        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        self.assertEqual([1, 2, 4], iter_list(sol.plusOne(node1)))

        node1 = ListNode(1)
        node2 = ListNode(2)
        node9 = ListNode(9)
        node1.next = node2
        node2.next = node9

        self.assertEqual([1, 3, 0], iter_list(sol.plusOne(node1)))

        node1 = ListNode(9)
        node2 = ListNode(9)
        node9 = ListNode(9)
        node1.next = node2
        node2.next = node9

        self.assertEqual([1, 0, 0, 0], iter_list(sol.plusOne(node1)))


if __name__ == '__main__':
    unittest.main()
