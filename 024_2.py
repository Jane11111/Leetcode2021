# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 21:08
# @Author  : zxl
# @FileName: 024_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:


        new_head = ListNode(-1)
        new_head.next = head
        pre = new_head

        p = head
        while p:
            p2 = p.next
            if not p2:
                break
            p3 = p2.next

            pre.next = p2
            p2.next = p
            p.next = p3

            pre = p
            p = p3
        return new_head.next



