# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 21:53
# @Author  : zxl
# @FileName: 023_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists ) :

        head = ListNode(-1)
        p = head


        while True :
            idx = -1
            i = 0
            cur_val = 10000
            while i< len(lists):

                if lists[i] != None :
                    if idx == -1 or lists[i].val<cur_val:
                        idx = i
                        cur_val = lists[i].val
                    i+=1
                else:
                    lists.pop(i)
            if idx == -1:
                break

            p.next = lists[idx]
            lists[idx] = lists[idx].next
            p = p.next
        return head.next


