# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 11:34
# @Author  : zxl
# @FileName: 138_2.py



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head == None:
            return None

        p = head
        while p:
            new_p = Node(p.val)
            new_p.next = p.next
            p.next = new_p
            p = p.next.next

        p = head

        while p:
            if p.random == None:
                p = p.next.next
                continue
            p.next.random = p.random.next
            p = p.next.next


        new_head = head.next
        p = new_head
        while p and p.next:
            p.next = p.next.next
            p = p.next
        return new_head



