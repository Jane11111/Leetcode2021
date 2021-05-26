# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 10:00
# @Author  : zxl
# @FileName: 023_5.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue
class Solution:

    def merge(self,l1,l2):

        head = ListNode(-1)
        p = head

        p1 =l1
        p2 = l2
        while p1 or p2:
            if p1 == None:
                p.next = p2
                break
            if p2 == None:
                p.next = p1
                break
            if p1.val<p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        return head.next

    def mergeLists(self,lists,left,right):
        if left == right:
            return lists[left]
        if left>right:
            return None
        mid = (left+right)//2
        l1 = self.mergeLists(lists,left,mid)
        l2 = self.mergeLists(lists,mid+1,right)
        l = self.merge(l1,l2)
        return l

    def mergeKLists(self, lists ) :

        p = self.mergeLists(lists,0,len(lists)-1)
        return p


