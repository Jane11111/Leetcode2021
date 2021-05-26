# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 15:10
# @Author  : zxl
# @FileName: 002.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


        head = ListNode(-1)
        p = head
        base = 0

        while l1 or l2:
            if l1:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0

            if l2:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            n = n1+n2+base

            p.next = ListNode(n%10)
            p = p.next
            base = n//10
        if base:
            p.next = ListNode(base)
        return head.next
