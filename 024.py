# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 21:39
# @Author  : zxl
# @FileName: 024.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        res = head.next
        p = head
        last = ListNode()
        while p != None and p.next != None:
            tmp = p.next
            last.next = tmp # 需要注意这句话，把上一个pair的指针指向新的下一个pair
            p.next = p.next.next
            tmp.next = p
            last = p
            p = p.next
        return res