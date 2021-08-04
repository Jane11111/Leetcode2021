# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 09:48
# @Author  : zxl
# @FileName: 086_2.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:


        newhead = ListNode(-1)
        newhead.next = head

        last_p = newhead
        p = head
        pre = newhead
        while p:



            if p.val<x:

                # if last_p == pre:
                #     last_p = p
                #     p = p.next
                #     pre = pre.next
                #     continue

                pre.next = p.next


                p.next = last_p.next
                last_p.next = p

                last_p = p
                p = pre.next# 遍历下一个节点
            else:
                pre = pre.next
                p = p.next
        return newhead.next

p1 = ListNode(1)
p2 = ListNode(2)
p4 = ListNode(4)

p1.next = p4
p4.next = p2

obj = Solution()
p = obj.partition(p1,4)
print(p)

