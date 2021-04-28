# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 21:37
# @Author  : zxl
# @FileName: I0208.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:


        p1 = head
        p2 = head

        while p2:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
            else:
                continue
            if p1==p2:
                p2 = head
                while p1!=p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1

        return None



