# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 13:02
# @Author  : zxl
# @FileName: 538.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveUpdate(self,root,n):

        if root == None:
            return 0
        v = root.val
        s = self.recursiveUpdate(root.right,n)
        root.val = n + s + root.val
        l = self.recursiveUpdate(root.left,root.val)
        return s+l+v


    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.recursiveUpdate(root,0)

        return root

