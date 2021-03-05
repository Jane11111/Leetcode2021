# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 22:02
# @Author  : zxl
# @FileName: 019.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        count = 0
        p = head
        while p != None:
            p = p.next
            count += 1
        if n == count:
            return head.next

        l = count - n
        i = 1
        p = head
        while i<l:
            p = p.next
            i += 1
        p.next = p.next.next
        return head