# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 20:55
# @Author  : zxl
# @FileName: 023_8.py




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:

    def mergeKLists(self, lists) -> ListNode:

        if len(lists) == 0:
            return None

        lst = []

        for i in range(len(lists)):

            p = lists[i]
            if p:
                heapq.heappush(lst,[p.val,i])
                # lists[i] = lists[i].next

        new_head = ListNode(-1)
        p = new_head

        while len(lst)>0:
            v,idx = heapq.heappop(lst)


            p.next = lists[idx]
            lists[idx] = lists[idx].next

            if lists[idx] :
                heapq.heappush(lst,[lists[idx].val,idx])

            p = p.next
        return new_head.next


