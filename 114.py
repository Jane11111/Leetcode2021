# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 21:33
# @Author  : zxl
# @FileName: 114.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def recFlatten(self,root):

        if root == None:
            return None,None
        lh,lt = self.recFlatten(root.left)
        rh,rt = self.recFlatten(root.right)
        root.left = None
        if lh:
            root.right = lh
            lt.right = rh

        else:
            root.right = rh

        l = root
        r = root
        if rt:
            r = rt
        elif lt:
            r = lt
        return l,r



    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        h,t = self.recFlatten(root)
        return h




