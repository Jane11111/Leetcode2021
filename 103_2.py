# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 13:52
# @Author  : zxl
# @FileName: 103_2.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) :


        Q = [root] if root else []
        ans = []
        l2r = True

        while len(Q)>0:

            n = len(Q)
            lst = []
            while n:
                n-=1
                p = Q.pop(0)
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
                if l2r:
                    lst.append(p.val)
                else:
                    lst.insert(0,p.val)
            l2r = not l2r
            ans.append(lst)
        return ans