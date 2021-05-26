# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 13:20
# @Author  : zxl
# @FileName: 876_2.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:


        slow = head
        fast = head

        while fast:
            if fast.next:
                slow = slow.next
                fast = fast.next
            if fast:
                fast = fast.next
        return slow



