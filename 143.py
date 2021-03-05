# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:04
# @Author  : zxl
# @FileName: 143.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head

        arr = []
        p = head
        while p:
            arr.append(p)
            p = p.next
            arr[-1].next = None
        i = 0
        j = len(arr) - 1
        while j-i >= 1:
            if j-i == 1:
                arr[i].next = arr[j]
            else:
                arr[i].next = arr[j]
                arr[j].next = arr[i+1]
            i += 1
            j -= 1
        return arr[0]

