# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 22:08
# @Author  : zxl
# @FileName: 23_3.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists ) :

        if len(lists) == 0:
            return None


        l = 0
        r = len(lists)-1

        while r != 0:

            while l<r:

                head = ListNode(-1)
                p = head
                while lists[l] != None or lists[r] !=None:
                    if lists[l]  == None:
                        p.next = lists[r]
                        break
                    elif lists[r]  == None:
                        p.next = lists[l]
                        break
                    if lists[l].val<lists[r].val:
                        p.next = lists[l]
                        lists[l] = lists[l].next
                    else:
                        p.next = lists[r]
                        lists[r] = lists[r].next
                    p = p.next
                lists[l] = head.next
                l+=1
                r-=1

            r = l
            l = 0
        return lists[l]


