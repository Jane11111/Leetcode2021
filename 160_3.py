# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 11:04
# @Author  : zxl
# @FileName: 160_3.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:



        p = headA
        q = headB

        while p!=q:

            p = p.next if p else headB
            q = q.next if q else headA
        return p
