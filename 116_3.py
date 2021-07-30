# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 10:21
# @Author  : zxl
# @FileName: 116_3.py



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
            return

        p = root
        while p and p.left:
            p.left.next = p.right
            if p.next:
                p.right.next = p.next.left
            p = p.next
        self.connect(root.left)
        return root


