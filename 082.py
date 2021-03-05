# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 22:23
# @Author  : zxl
# @FileName: 082.py

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
        new_head = ListNode(-101)
        new_head.next = head
        last = new_head
        p = last.next
        while p != None and p.next != None:
            if p.val == p.next.val:
                while p.next != None and p.val == p.next.val:
                    p = p.next
                last.next = p.next
                p = p.next

            else:
                last = p
                p = p.next
        return new_head.next

