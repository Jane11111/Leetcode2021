# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 16:52
# @Author  : zxl
# @FileName: 019_3.py





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


        new_head = ListNode(-1)
        new_head.next = head

        p = new_head
        lst = []
        while p:
            lst.append(p)
            p = p.next

        p = lst[-n-1]
        p.next = p.next.next
        return new_head.next
