# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 12:44
# @Author  : zxl
# @FileName: 099.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

