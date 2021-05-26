# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 20:55
# @Author  : zxl
# @FileName: 098_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def dfs(self,root,min_val,max_val):
        if root == None:
            return True
        if root.val<=min_val or root.val>=max_val:
            return False

        f1 = self.dfs(root.left,min_val,root.val)
        f2 = self.dfs(root.right,root.val,max_val)
        return f1 and f2

    def isValidBST(self, root: TreeNode) -> bool:


        return self.dfs(root,float('-inf'),float('inf'))


