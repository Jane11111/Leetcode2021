# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 09:36
# @Author  : zxl
# @FileName: 142.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = 200001
        p = head
        res = None
        while p != None:
            if p.val >= 100001:
                res = p
                break
            p.val += num
            p = p.next
        #还原
        p = head
        if p != None:
            p.val -= num
        while p != None and p != res:
            p = p.next
            if p != None:
                p.val -= num
        return res




