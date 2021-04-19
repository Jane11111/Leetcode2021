# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 11:15
# @Author  : zxl
# @FileName: 138.py




# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':


        if head == None:
            return head

        p = head

        dic1 = {}
        dic2 = {}
        idx = 0
        while p:
            dic1[p] = idx
            new_p = Node(p.val)
            dic2[idx] = new_p
            idx+=1
            p = p.next
        p = head
        for i in range(idx):
            if i<idx-1:
                dic2[i].next = dic2[i+1]

            if p.random == None:
                p = p.next
                continue
            random_idx = dic1[p.random]
            dic2[i].random = dic2[random_idx]

            p = p.next
        return dic2[0]
