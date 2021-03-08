# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 14:36
# @Author  : zxl
# @FileName: 563.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveUpdate(self,root):
        if root == None:
            return 0
        l = self.recursiveUpdate(root.left)
        r = self.recursiveUpdate(root.right)
        s = l + r + root.val
        root.val = abs(l-r)
        return s


    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.recursiveUpdate(root)

        if root == None:
            return 0
        l = self.recursiveUpdate(root.left)
        r = self.recursiveUpdate(root.right)
        return l+r+root.val

