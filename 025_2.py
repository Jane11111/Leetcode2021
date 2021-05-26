# -*- coding: utf-8 -*-
# @Time    : 2021-05-21 14:05
# @Author  : zxl
# @FileName: 025_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:



        if k<=1:
            return head

        new_head = ListNode(-1)
        new_head.next = head

        last_tail = new_head

        # pre = last_tail

        while last_tail:
            pre = last_tail

            p = pre.next
            count = 1
            while p and count<=k:
                p = p.next
                count+=1
            if count<=k:
                break

            p = pre.next
            tmp = p
            count = 1
            while count<=k:
                post = p.next
                p.next = pre
                pre = p
                p = post
                count+=1
            last_tail.next = pre
            last_tail = tmp
            last_tail.next = p
        return new_head.next









