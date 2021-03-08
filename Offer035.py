# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 20:39
# @Author  : zxl
# @FileName: Offer035.py


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

        if head == None:
            return head
        p = head
        arr = []
        idx = 0
        dic = {}
        while p:
            arr.append(Node(p.val))
            dic[p] = idx
            p = p.next
            idx += 1

        p = head
        idx = 0
        while p:
            if p.random == None:
                arr[idx].random = None
            else:
                pos = dic[p.random]
                arr[idx].random = arr[pos]
            idx += 1
            p = p.next
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        return arr[0]


