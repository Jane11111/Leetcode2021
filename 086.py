# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 22:43
# @Author  : zxl
# @FileName: 086.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        new_head = ListNode(x-1)
        new_head.next = head
        p1 = new_head
        last = p1
        cur = last.next
        while cur != None:
            if cur.val < x:
                if p1 != last:
                    last.next = cur.next

                    cur.next = p1.next
                    p1.next = cur
                    p1 = cur
                else:
                   last = cur
                   p1 = cur

                cur = last.next

            else:
                last = cur
                cur = cur.next
        return new_head.next