# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 11:45
# @Author  : zxl
# @FileName: 129_4.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recSum(self,root,val):

        if not root:
            return val
        if not root.left and not root.right:
            return val+root.val
        l = 0
        if root.left:
            l = self.recSum(root.left,(val+root.val)*10)
        r = 0
        if root.right:
            r = self.recSum(root.right,(val+root.val)*10)
        return l+r

    def sumNumbers(self, root: TreeNode) -> int:


        ans = self.recSum(root,0)
        return ans


