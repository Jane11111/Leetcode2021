# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 21:14
# @Author  : zxl
# @FileName: 024_3.py




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next

        p3 = self.swapPairs(p2.next)
        p2.next = p1
        p1.next = p3
        return p2

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next = p2
p2.next = p3
p3.next = p4
obj = Solution()
ans = obj.swapPairs(p1)
print(ans)
