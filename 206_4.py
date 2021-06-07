# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 17:46
# @Author  : zxl
# @FileName: 206_4.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:



        p1 = head
        if not p1 or not p1.next:
            return p1

        p2 = p1.next
        p1.next = None
        while p2:

            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1
