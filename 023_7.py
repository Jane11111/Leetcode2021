# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 18:01
# @Author  : zxl
# @FileName: 023_7.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self,p1,p2):

        head = ListNode(-1)
        p = head

        while p1 or p2:

            if not p1 or (p1 and p2 and p2.val<=p1.val):
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        return head.next



    def mergeKLists(self, lists ) -> ListNode:


        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        m = (len(lists)-1)//2
        p1 = self.mergeKLists(lists[:m+1])
        p2 = self.mergeKLists(lists[m+1:])
        p = self.mergeTwoLists(p1,p2)
        return p
