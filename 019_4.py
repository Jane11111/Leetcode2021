# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 16:55
# @Author  : zxl
# @FileName: 019_4.py






# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head , n: int)  :

        new_head = ListNode(-1)
        new_head.next = head

        p = new_head
        while p:
            tmp = p
            for i in range(n+1):
                tmp = tmp.next
            if tmp == None:
                p.next = p.next.next
                break
            p = p.next
        return new_head.next
