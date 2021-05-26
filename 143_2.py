# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 12:57
# @Author  : zxl
# @FileName: 143_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """



        cnt = 0
        p = head

        while p:
            cnt+=1
            p = p.next

        if cnt<=2:
            return


        m = cnt//2
        cnt = 0
        p = head
        while cnt!=m:
            p = p.next
            cnt +=1
        head2 = p.next
        p.next = None


        pre = head2
        cur = pre.next
        pre.next = None
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        p1 = head
        p2 = pre

        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2





