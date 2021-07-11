# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 17:09
# @Author  : zxl
# @FileName: 021_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_head = ListNode(-1)
        p = new_head

        while l1 or l2:

            if not l1 or (l1 and l2 and l2.val<=l1.val):
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        return new_head.next


