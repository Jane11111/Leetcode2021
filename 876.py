# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 19:40
# @Author  : zxl
# @FileName: 876.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        m = int(count/2)
        p = head
        for i in range(m):
            p = p.next
        return p