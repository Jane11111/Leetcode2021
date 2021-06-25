# -*- coding: utf-8 -*-
# @Time    : 2021-06-24 21:28
# @Author  : zxl
# @FileName: 404.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recSum(self,root):

        if not root:
            return 0,False


        if not root.left and not root.right:
            return root.val, True


        l = 0
        if root.left:
            l,f = self.recSum(root.left)

        if root.right:
            r,f2 = self.recSum(root.right)

            if not f2:
                l+=r
        return l,False

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        ans,f = self.recSum(root)
        if f:
            ans = 0
        return ans


