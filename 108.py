# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 21:16
# @Author  : zxl
# @FileName: 108.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums ) -> TreeNode:


        if len(nums) == 0:
            return None

        m = (len(nums)-1)//2

        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])
        return root