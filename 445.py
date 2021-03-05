# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 16:54
# @Author  : zxl
# @FileName: 445.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def getNum(self,l1):
        p = l1
        arr = []
        while p:
            arr.insert(0,p.val)
            p = p.next
        res = 0
        base = 1
        for i in range(len(arr)):
            res += arr[i] * base
            base *= 10
        return res


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.getNum(l1)
        n2 = self.getNum(l2)

        n = n1+n2

        base = 10
        m  = n%base
        n = int((n-m)/base)
        p = ListNode(m)
        while n:
            m = n % base
            n = int((n - m) / base)
            p1 = ListNode(m)
            p1.next = p
            p = p1
        return p

obj = Solution()
l1 = ListNode(7)
l1.next = ListNode(1)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(8)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
res = obj.addTwoNumbers(l1,l2)
print(res)