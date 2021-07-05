# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 15:23
# @Author  : zxl
# @FileName: 002_2.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


        head = ListNode(0)
        p = head
        base = 0
        while l1 or l2:
            if not l1:
                n1 = 0
            else :
                n1 = l1.val
                l1 = l1.next

            if not l2:
                n2 = 0
            else:
                n2 = l2.val
                l2 = l2.next

            v = (n1+n2+base)
            base = v//10
            p.next = ListNode(v%10)
            p = p.next
        if base:
            p.next = ListNode(base)
            p = p.next
        return head.next


