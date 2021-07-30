# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 11:02
# @Author  : zxl
# @FileName: 117_3.py

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        p = root
        last = None
        tmp = None
        while p and not last:
            last = p.left
            tmp = last
            if not last:
                last = p.right
                p = p.next
                tmp = last
            else:
                if p.right:
                    last.next = p.right
                    last = p.right
                p = p.next


        while p:
            if p.left:
                last.next = p.left
                last = p.left
            if p.right:
                last.next = p.right
                last = p.right
                p = p.next
            else:
                p = p.next

        self.connect(tmp)
        return root


