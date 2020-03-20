from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        [369. Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list)

        Given a non-negative number represented as a singly linked list of digits, plus one to the number.

        The digits are stored such that the most significant digit is at the head of the list.

        **Example:**

        ```
        Input:
        1->2->3

        Output:
        1->2->4
        ```

        References
        ---------
        .. [1] https://leetcode.com/articles/plus-one-linked-list/
        """
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1

        not_nine = not_nine.next
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        return dummy if dummy.val else dummy.next
