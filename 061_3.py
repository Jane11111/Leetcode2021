# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 14:00
# @Author  : zxl
# @FileName: 061_3.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:



        count = 0
        p = head
        tail = p

        while p:
            count+=1
            tail = p
            p = p.next
        if count <= 1 or k%count == 0:
            return head

        k%= count
        k = count - k

        count = 1
        p = head
        while count!=k:
            p = p.next
            count+=1

        newhead = p.next
        p.next = None
        tail.next = head
        return newhead
