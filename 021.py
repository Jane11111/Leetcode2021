# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 10:33
# @Author  : zxl
# @FileName: 021.py

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        head = res
        p = res

        while l1!= None or l2!= None:
            if l1  == None:
                p.next = l2
                l2 = None
            elif l2 == None:
                p.next = l1
                l1 = None
            else:
                if l1.val <= l2.val:
                    p.next = l1
                    p = p.next
                    l1 = l1.next
                else:
                    p.next = l2
                    p = p.next
                    l2 = l2.next
        return head.next