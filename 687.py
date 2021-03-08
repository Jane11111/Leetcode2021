# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 14:52
# @Author  : zxl
# @FileName: 687.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0
