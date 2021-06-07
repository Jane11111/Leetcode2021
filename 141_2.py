# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 11:15
# @Author  : zxl
# @FileName: 141_2.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:


        slow = head
        if not slow or not slow.next or not slow.next.next:
            return False
        fast = slow.next.next
        while slow!=fast:
            slow = slow.next
            if not fast.next or not fast.next.next:
                return False
            else:
                fast = fast.next.next
        return True