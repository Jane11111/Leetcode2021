# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 22:54
# @Author  : zxl
# @FileName: I0206.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        count = 0
        p = head
        while p:
            count+=1
            p = p.next

        if count <= 1:
            return True

        m = count//2

        n = 1
        last = head
        cur = head.next

        while n!=m:
            last = last.next
            cur = cur.next
            n+=1

        last.next = None
        p1 = cur
        p2 = p1.next
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        p = head
        while p and p1:
            if p.val!=p1.val:
                return False
            p = p.next
            p1 = p1.next
        return True

