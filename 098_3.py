# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 16:13
# @Author  : zxl
# @FileName: 098_3.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recFind(self,root,min_val,max_val):

        if not root:
            return True
        if root.val<=min_val or root.val>=max_val:
            return False
        f1 = self.recFind(root.left,min_val,min(max_val,root.val))
        f2 = self.recFind(root.right,max(min_val,root.val),max_val)
        return f1 and f2


    def isValidBST(self, root: TreeNode) -> bool:

        ans = self.recFind(root,float('-inf'),float('inf'))
        return ans