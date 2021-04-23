# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 22:15
# @Author  : zxl
# @FileName: 222.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        Q = [root] if  root else []
        while len(Q)>0:
            l = len(Q)

            count += l
            i = 0
            while i<l:
                p = Q.pop(0)
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
                i+=1
        return count