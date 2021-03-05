# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:47
# @Author  : zxl
# @FileName: 203.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        new_head = ListNode(0,head)
        last = new_head
        p = new_head.next
        while p != None:
            if p.val == val:
                last.next = p.next
                p = p.next
            else:
                last = last.next
                p = p.next
        return new_head.next