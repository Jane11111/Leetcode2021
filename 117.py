# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 16:11
# @Author  : zxl
# @FileName: 117.py




# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        lst = []
        if root:
            lst.append(root)
        while len(lst) > 0:

            l = len(lst)
            for i in range(l-1):
                p = lst.pop(0)
                p.next = lst[0]
                if p.left:
                    lst.append(p.left)
                if p.right:
                    lst.append(p.right)
            p = lst.pop(0)
            if p.left:
                lst.append(p.left)
            if p.right:
                lst.append(p.right)
        return root