# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 23:14
# @Author  : zxl
# @FileName: 092.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if left >= right:
            return head

        new_head = ListNode(-1)
        new_head.next = head
        i = 0
        p = new_head
        while p != None:
            if i == left-1:
                pre = p
                sub_tail = pre.next
            elif i == right :
                sub_head = p
                post = p.next
            i += 1
            p = p.next
        last = pre.next
        cur = pre.next.next
        while cur != None and cur != post:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        sub_tail.next = post
        pre.next = sub_head
        return new_head.next




