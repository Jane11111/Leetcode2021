# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 15:30
# @Author  : zxl
# @FileName: 061_2.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        count = 0
        p = head
        while p:
            count+=1
            p = p.next

        k = k%count
        if k == 0:
            return head

        p = head
        fast = p
        while k:
            fast = fast.next
            k -= 1

        while fast.next:
            p = p.next
            fast = fast.next

        new_head = p.next
        p.next = None
        fast.next = head
        return new_head
