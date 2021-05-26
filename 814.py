# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 20:26
# @Author  : zxl
# @FileName: 814.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:


        if not root:
            return root

        l = self.pruneTree(root.left)
        r = self.pruneTree(root.right)

        if not l and not r and not root.val:
            return None
        root.left = l
        root.right = r
        return root









