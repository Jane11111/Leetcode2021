# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 20:29
# @Author  : zxl
# @FileName: Offer022.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        count = 0
        p = head
        while p:
            p = p.next
            count += 1

        p = head
        for i in range(count-k):
            p = p.next
        return p

