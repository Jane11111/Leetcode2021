# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 10:21
# @Author  : zxl
# @FileName: 100.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def dfs(self,p1,p2):
        if p1 == None and p2 == None:
            return True
        if p1 == None:
            return False
        if p2 == None:
            return False
        if p1.val != p2.val:
            return False

        f1 = self.dfs(p1.left,p2.left)
        f2 = self.dfs(p1.right,p2.right)
        return f1 and f2

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return self.dfs(p,q)
