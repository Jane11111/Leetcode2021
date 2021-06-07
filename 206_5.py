# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 17:56
# @Author  : zxl
# @FileName: 206_5.py




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def recReverse(self,head):


        if not head:
            return None,None
        if not head.next:
            return head,head

        h,t = self.recReverse(head.next)
        t.next = head
        head.next = None
        return h,head

    def reverseList(self, head: ListNode) -> ListNode:

        h,t = self.recReverse(head)
        return h
