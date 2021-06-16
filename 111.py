# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 21:21
# @Author  : zxl
# @FileName: 111.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0

        if not root.left and not root.right:
            return 1

        l = float('inf')
        r = float('inf')
        if root.left:
            l = self.minDepth(root.left)
        if root.right:
            r = self.minDepth(root.right)

        return min(l,r)+1


