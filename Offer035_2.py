# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 20:55
# @Author  : zxl
# @FileName: Offer035_2.py


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head == None or head.next == None:
            return head

        p = head
        while p:
            tmp = p.next
            p.next = Node(p.val)
            p.next.next = tmp
            p = tmp
        p = head
        while p:
            if p.random == None:
                p.next.random = None

            else:
                p.next.random = p.random.next
            p = p.next.next
        new_head = head.next
        p = new_head
        while p.next:
            p.next = p.next.next
            p = p.next
        return new_head
