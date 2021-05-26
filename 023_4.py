# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 09:47
# @Author  : zxl
# @FileName: 023_4.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists ) :

        q = PriorityQueue()

        for i in range(len(lists)):
            if lists[i]:
                q.put([lists[i].val, i])
            # lists[i] = lists[i].next

        head = ListNode(-1)
        p = head

        while q.qsize()>0:

            v, idx = q.get()
            p.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                q.put([lists[idx].val, idx])

            p = p.next
        return head.next


