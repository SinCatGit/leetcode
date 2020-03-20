import unittest
from insert_into_a_cyclic_sorted_list import Solution, ListNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        head = ListNode(3)
        node5 = ListNode(5)
        node1 = ListNode(1)
        node2 = ListNode(2)

        head.next = node5
        node5.next = node1
        node1.next = node2
        node2.next = head
        head = sol.insert(head, 7)
        current = head.next
        res = [head.val]
        while current is not head:
            res.append(current.val)
            current = current.next
        self.assertEqual([3, 5, 7, 1, 2], res)


if __name__ == '__main__':
    unittest.main()
