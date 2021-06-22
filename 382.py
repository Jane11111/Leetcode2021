# -*- coding: utf-8 -*-
# @Time    : 2021-06-21 17:36
# @Author  : zxl
# @FileName: 382.py


import random
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """

        p = head
        count = 1
        while p.next:
            p = p.next
            count+=1

        p.next = head
        self.p = p
        self.count = count


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n = random.random()
        while n>1/self.count:
            n = random.random()
            self.p = self.p.next
        return self.p.val

