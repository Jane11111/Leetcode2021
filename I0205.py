# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 22:05
# @Author  : zxl
# @FileName: I0205.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_head = ListNode(0)
        p = new_head

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
            base = n//10
            p = p.next
        if base:
            p.next = ListNode(base)
        return new_head.next
