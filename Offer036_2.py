# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 10:45
# @Author  : zxl
# @FileName: Offer036_2.py



# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def recTrans(self,root):
        if root == None:
            return None,None

        lh,lt = self.recTrans(root.left)
        rh,rt = self.recTrans(root.right)

        if lh == None:
            head = root
        else:
            head = lh
            lt.right = root
            root.left = lt
        if rh == None:
            tail = root
        else:
            tail = rt
            root.right = rh
            rh.left = root
        return head,tail

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        head,tail = self.recTrans(root)

        if head:
            head.left = tail
            tail.right = head
        return head