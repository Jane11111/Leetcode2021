# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 19:34
# @Author  : zxl
# @FileName: 817.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """