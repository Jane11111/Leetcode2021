# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 16:35
# @Author  : zxl
# @FileName: 142_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:


        if head == None:
            return head

        slow = head.next
        if not slow:
            return None
        fast = head.next.next

        while fast and slow!=fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next

        if not fast:
            return fast
        fast = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow

