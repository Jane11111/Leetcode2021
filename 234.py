# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:56
# @Author  : zxl
# @FileName: 234.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        p = head
        while p != None:
            arr.append(p.val)
            p = p.next
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True