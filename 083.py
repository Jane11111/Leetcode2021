# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 22:37
# @Author  : zxl
# @FileName: 083.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p != None and p.next != None:
            if p.val == p.next.val:
                first = p
                while p.next != None and p.val == p.next.val:
                    p = p.next
                first.next = p.next
                p = p.next
            else:
                p = p.next
        return head