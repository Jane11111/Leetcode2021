# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:42
# @Author  : zxl
# @FileName: 160.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = {}
        p = headA
        while p != None:
            dic[p] = True
            p = p.next
        p = headB
        while p != None:
            if p in dic:
                return p
            p = p.next
        return None