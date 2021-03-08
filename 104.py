# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 12:08
# @Author  : zxl
# @FileName: 104.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l+1,r+1)