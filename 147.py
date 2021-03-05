# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:14
# @Author  : zxl
# @FileName: 147.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None :
            return head

        last = head
        p = head.next
        while p != None:
            if p.val >= last.val:
                last = p
                p = p.next
            else:
                last.next = p.next
                if head.val >= p.val:
                    p.next = head
                    head = p
                else:
                    pre = head
                    post = head.next
                    while post.val < p.val:
                        pre = pre.next
                        post = post.next
                    pre.next = p
                    p.next = post

                p = last.next
        return head
