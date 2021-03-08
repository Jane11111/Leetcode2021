# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 20:33
# @Author  : zxl
# @FileName: Offer024.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head
        last = head
        p = head.next
        last.next = None
        while p:
            tmp = p.next
            p.next = last
            last = p
            p = tmp
        return last