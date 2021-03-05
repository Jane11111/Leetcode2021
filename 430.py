# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 11:30
# @Author  : zxl
# @FileName: 430.py


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):

    def recursiveFlatten(self,p):
        head = p
        last = head
        while p:
            if p.child:
                sub_head, sub_tail = self.recursiveFlatten(p.child)

                sub_tail.next = p.next
                if p.next: # 注意p可能是最后一个
                    p.next.prev = sub_tail
                p.next = sub_head
                sub_head.prev = p
                p.child = None

                last = sub_tail
                p = sub_tail.next
            else:
                last = p
                p = p.next
        return head,last

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        head,last = self.recursiveFlatten(head)
        return head