# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 14:10
# @Author  : zxl
# @FileName: 445_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def strAdd(self,s1,s2):
        i = len(s1)-1
        j = len(s2)-1
        base = 0
        ans = ''
        while i>=0 or j>=0 :
            n1 = 0 if i<0 else int(s1[i])
            n2 = 0 if j<0 else int(s2[j])

            v = n1+n2+base
            ans = str(v%10)+ans
            base = v//10
            i-=1
            j-=1
        if base:
            ans=str(base)+ans
        return ans

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        s1 = ''
        s2 = ''
        while l1:
            s1+= str(l1.val)
            l1 = l1.next
        while l2:
            s2+=str(l2.val)
            l2= l2.next

        ans = self.strAdd(s1,s2)
        head = ListNode(-1)
        p = head
        for i in range(len(ans)):
            p.next = ListNode(int(ans[i]))
            p = p.next
        return head.next





