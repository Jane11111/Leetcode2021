# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 13:18
# @Author  : zxl
# @FileName: Offer028_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def solve(self,l,r):
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        return l.val == r.val and self.solve(l.left,r.right) and self.solve(l.right,r.left)




    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.solve(root.left,root.right)
