# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 22:28
# @Author  : zxl
# @FileName: I0207.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:


        if not headA or not headB:
            return None

        p = headA

        while p.next:
            p = p.next
        p.next = headA
        tail = p

        p1 = headB
        p2 = headB

        while p2:
            p1 = p1.next
            p2 = p2.next

            if p2:
                p2 = p2.next
            else:
                continue

            if p1 == p2:
                p2 = headB

                while p2!=p1:
                    p1 = p1.next
                    p2 = p2.next
                tail.next = None

                return p2
        tail.next = None
        return None



