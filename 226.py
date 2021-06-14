# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 16:25
# @Author  : zxl
# @FileName: 226.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:


        if root == None:
            return root

        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left = r
        root.right = l
        return root