# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 21:50
# @Author  : zxl
# @FileName: 206_2.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:


        if not head:
            return head

        p1 = head
        p2 = head.next
        p1.next = None
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        return p1