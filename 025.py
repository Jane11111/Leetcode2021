# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 18:01
# @Author  : zxl
# @FileName: 025.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        last_p = ListNode(-1)
        new_head = last_p

        p = head
        while p:

            p1 = p
            count = 1
            while p and count<k:
                p= p.next
                count +=1
            if count<k or not p:
                last_p.next = p1
                break
            tmp = p.next
            last_p.next = p
            last_p = p1

            p2 = p1.next


            while p2!=tmp:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3

            p = tmp
            last_p.next = None

        return new_head.next

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p1.next = p2
# p2.next = p3
# p3.next = p4
# p4.next = p5

obj = Solution()
p = obj.reverseKGroup(p1,2)

while p:
    print(p.val)
    p = p.next

