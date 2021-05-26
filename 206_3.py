# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 21:53
# @Author  : zxl
# @FileName: 206_3.py




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def recursiveReverse(self,head):
        if head == None:
            return None,None

        p = head
        h,t = self.recursiveReverse(head.next)
        if not h and not t:
            return p,p
        t.next = p
        p.next = None
        return h,p

    def reverseList(self, head: ListNode) -> ListNode:


        h,t = self.recursiveReverse(head)
        return h




