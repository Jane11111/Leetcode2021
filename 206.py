# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:50
# @Author  : zxl
# @FileName: 206.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return head
        p1 = head
        p2 = p1.next
        while p2 != None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        head.next = None
        return p1