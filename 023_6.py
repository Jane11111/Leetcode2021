# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 17:33
# @Author  : zxl
# @FileName: 023_6.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self,p1,p2):

        head = ListNode(-1)
        p = head

        while p1 or p2:

            if not p1 or (p1 and p2 and p2.val<=p1.val):
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        return head.next



    def mergeKLists(self, lists ) -> ListNode:

        if len(lists) == 0:
            return None

        while len(lists)>1:

            tmp = []

            l = 0
            r = len(lists)-1
            while l<=r:
                if l == r:
                    p = lists[l]
                else:

                    p = self.mergeTwoLists(lists[l],lists[r])
                tmp.append(p)
                l+=1
                r-=1
            lists = tmp
        return lists[0]