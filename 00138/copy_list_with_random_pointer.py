from typing import List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        https://leetcode.com/problems/copy-list-with-random-pointer

        A linked list is given such that each node contains an additional random pointer
        which could point to any node in the list or null.

        Return a deep copy of the list.

        The Linked List is represented in the input/output as a list of n nodes. Each node
        is represented as a pair of [val, random_index] where:

        val: an integer representing Node.val
        random_index: the index of the node (range from 0 to n-1) where random pointer points
        to, or null if it does not point to any node.

        Example 1:

        Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


        Example 2:

        Input: head = [[1,1],[2,1]]
        Output: [[1,1],[2,1]]


        Example 3:

        Input: head = [[3,null],[3,0],[3,null]]
        Output: [[3,null],[3,0],[3,null]]


        Example 4:

        Input: head = []
        Output: []
        Explanation: Given linked list is empty (null pointer), so return null.

        Parameters
        ----------
        head: Node

        Returns
        -------
        Node

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
        .. [2] https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43689/Python-solution-without-using-dictionary.
        .. [3] https://www.cnblogs.com/zuoyuan/p/3745126.html

        """
        from collections import defaultdict
        d = defaultdict(lambda: Node(0))
        d[None] = None
        current = head
        while current:
            d[current].val = current.val
            d[current].next = d[current.next]
            d[current].random = d[current.random]
            current = current.next
        return d[head]

    def copyRandomListV01(self, head: Node) -> Node:
        d = {}
        current = head
        while current:
            d[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            d[current].next = d.get(current.next, None)
            d[current].random = d.get(current.random, None)
            current = current.next

        return d[head]

    def copyRandomListV02(self, head: Node) -> Node:
        current = head
        while current:
            node = Node(current.val)
            node.next = current.next
            current.next = node
            current = node.next

        current = head
        while current:
            current.next.random = current.random and current.random.next
            current = current.next.next

        second = head.next
        current = head.next
        while current.next:
            head.next = current.next
            head = current.next
            current.next = head.next
            current = current.next
        head.next = None
        return second





