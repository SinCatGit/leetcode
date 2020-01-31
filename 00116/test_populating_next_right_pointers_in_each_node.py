import unittest
from populating_next_right_pointers_in_each_node import Solution, Node


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        node1 = Node(val=1)
        node2 = Node(val=2)
        node3 = Node(val=3)
        node4 = Node(val=4)
        node5 = Node(val=5)
        node6 = Node(val=6)
        node7 = Node(val=7)

        node1.left = node2
        node1.right = node3

        node2.left = node4
        node2.right = node5

        node3.left = node6
        node3.right = node7

        solution = Solution()
        r = solution.connect(node1)

        from collections import deque
        mq = deque()
        mq.append(r)
        mq.append(None)
        while r and mq:
            n = mq.popleft()

            if n:
                self.assertEqual(id(n.next), id(mq[0]))
                if n.left:
                    mq.append(n.left)

                if n.right:
                    mq.append(n.right)
            else:
                if len(mq) > 0:
                    mq.append(None)


if __name__ == '__main__':
    unittest.main()
