# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 23:17
# @Author  : zxl
# @FileName: Offer025.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        p1 = l1
        p2 = l2
        p = ListNode(0)
        head = p
        while p1 or p2:
            if p1 == None:
                p.next = p2
                p2 = None
                continue
            if p2 == None:
                p.next = p1
                p1 = None
                continue
            if p1.val<=p2.val:
                p.next = p1
                p1 = p1.next

            else:
                p.next = p2
                p2 = p2.next
            p = p.next
            p.next = None
        return head.next