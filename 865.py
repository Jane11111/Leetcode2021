# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 17:45
# @Author  : zxl
# @FileName: 865.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

