# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 11:12
# @Author  : zxl
# @FileName: 328.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        head1 = head
        head2 = head.next
        p1 = head1
        p2 = head2


        idx = 1
        p = head.next.next
        p1.next = None
        p2.next = None
        while p != None:
            tmp = p.next
            p.next = None
            if idx % 2:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            idx += 1
            p = tmp
        p1.next = head2
        return head1

