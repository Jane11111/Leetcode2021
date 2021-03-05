# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 20:26
# @Author  : zxl
# @FileName: Offer018.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        new_head = ListNode(0)
        new_head.next = head
        last = new_head
        p = head
        while p:
            if p.val == val:
                last.next = p.next
                p = p.next
            else:
                last = last.next
                p = p.next
        return new_head.next