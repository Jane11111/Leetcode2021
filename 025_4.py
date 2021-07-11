# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 21:39
# @Author  : zxl
# @FileName: 025_4.py




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:


        if k == 1:
            return head

        new_head = ListNode(-1)
        last_tail = new_head

        p1 = head
        while p1:

            count = 0
            p = p1
            while p and count<k:
                p = p.next
                count+=1

            if count<k:
                last_tail.next = p1
                break

            next_p = p

            p = p1
            pre = None
            while p!=next_p:
                p2 = p.next

                p.next = pre
                pre = p
                p = p2
            last_tail.next = pre
            last_tail = p1
            p1 = next_p
        return new_head.next



