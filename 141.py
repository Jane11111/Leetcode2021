# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 09:26
# @Author  : zxl
# @FileName: 141.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        p = head
        while p != None:
            if p.val == 200000:
                return True
            p.val = 200000
            p = p.next
        return False