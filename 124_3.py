# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 20:03
# @Author  : zxl
# @FileName: 124_3.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recFind(self,root):
        if not root:
            return float('-inf'),float('-inf')

        lsinglemax,lmax = self.recFind(root.left)
        rsinglemax,rmax = self.recFind(root.right)

        singlemax = max(max(lsinglemax,rsinglemax)+root.val,root.val)

        max_val = max(lmax,rmax,singlemax,lsinglemax+rsinglemax+root.val )

        # if root.left:
        #     max_val = max(max_val,lmax)
        # if root.right:
        #     max_val = max(max_val,rmax)

        return singlemax,max_val


    def maxPathSum(self, root: TreeNode) -> int:

        singlemax,max_val = self.recFind(root)
        return max_val


