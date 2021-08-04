# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 21:24
# @Author  : zxl
# @FileName: 082_2.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:


        newhead = ListNode(-1)

        last = newhead

        p = head

        while p:
            if p.next and p.next.val == p.val:
                val = p.val
                while p and p.val == val:
                    p = p.next
            else:
                last.next = p
                last = p
                p= p.next
                last.next = None
        return newhead.next


