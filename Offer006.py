# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 20:23
# @Author  : zxl
# @FileName: Offer006.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        p = head
        res = []
        while p:
            res.insert(0,p.val)
            p = p.next
        return res