# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 22:14
# @Author  : zxl
# @FileName: 061.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        count = 0
        p = head
        last_node = p
        while p != None:
            count += 1
            last_node = p
            p = p.next
        k = k%count
        if k == 0:
            return head
        l = count - k
        i = 1
        p = head
        while i<l:
            i += 1
            p = p.next
        last_node.next = head
        head = p.next
        p.next = None
        return head
