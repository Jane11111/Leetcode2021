# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 16:37
# @Author  : zxl
# @FileName: 160_2.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        p1 = headA
        p2 = headB

        while p1!=p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1