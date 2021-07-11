# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 21:23
# @Author  : zxl
# @FileName: 025_3.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if k == 1:
            return head

        count = 0
        p = head
        while p and count<k:
            p = p.next
            count += 1

        if count <k:
            return head


        pre = None
        p1 = head

        while p1!=p:
            p2 = p1.next
            p1.next = pre
            pre = p1

            p1 = p2

        head.next = self.reverseKGroup(p,k)
        return pre




