# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 15:29
# @Author  : zxl
# @FileName: 092_2.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:


    def reverse(self,head):

        tail = head

        p1 = None
        p2 = head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        head = p1
        return head,tail

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        newhead = ListNode(-1)
        newhead.next = head

        count = 1
        p = head
        pre = newhead

        p1 = None
        p2 = None
        p3 = None
        p4 = None
        while p:
            if count == left:
                p1 = pre
                p2 = p
            if count == right:
                p3 = p
                p4 = p.next
                break


            count+=1
            p = p.next
            pre = pre.next

        p3.next = None

        h,t = self.reverse(p2)
        p1.next = h
        t.next = p4
        return newhead.next




