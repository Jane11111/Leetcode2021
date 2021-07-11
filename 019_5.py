# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 17:01
# @Author  : zxl
# @FileName: 019_5.py




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd(self, head , n: int)  :

        new_head = ListNode(-1)
        new_head.next = head

        p1 = new_head
        p2 = p1
        for i in range(n+1):
            p2 = p2.next

        while p2!=None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return new_head.next

