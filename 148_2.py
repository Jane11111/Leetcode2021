# -*- coding: utf-8 -*-
# @Time    : 2021-06-03 22:24
# @Author  : zxl
# @FileName: 148_2.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:


    def mergeSort(self,head):
        p = head
        count = 0
        while p:
            count+=1
            p = p.next

        if count <=1:
            return head

        m = count // 2
        p = head
        idx = 0
        while idx!=m-1:
            p = p.next
            idx+=1

        p1 = head
        p2 = p.next
        p.next = None
        h1 = self.mergeSort(p1)
        h2 = self.mergeSort(p2)
        h = self.merge(h1,h2)

        return h




    def merge(self,p1,p2):

        p = ListNode()
        head = p

        while p1 or p2:
            if not p1:
                p.next = p2
                p2 = p2.next
            elif not p2:
                p.next = p1
                p1 = p1.next
            else:
                if p1.val<p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
            p = p.next
        return head.next


    def sortList(self, head: ListNode) -> ListNode:

        h = self.mergeSort(head)
        return h


