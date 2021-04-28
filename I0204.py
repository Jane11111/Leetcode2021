# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 22:12
# @Author  : zxl
# @FileName: I0204.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        p1 = ListNode(-1)
        p1.next = head
        new_head = p1


        last = p1
        p2 = head

        while p2:

            if p2.val>=x:
                p2 = p2.next
                last=last.next

            else:
                if last == p1:
                    p2=p2.next
                    last = last.next
                    p1 = p1.next
                else:
                    last.next = p2.next
                    p2.next = p1.next
                    p1.next = p2
                    p1 = p2
                    p2 = last.next
        return new_head.next

