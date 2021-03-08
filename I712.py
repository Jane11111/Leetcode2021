# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 16:49
# @Author  : zxl
# @FileName: I712.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root

        if not root.left:
            root.right = self.convertBiNode(root.right)
            return root
        new_root = self.convertBiNode(root.left)
        root.right = self.convertBiNode(root.right)
        root.left = None
        p = new_root
        while p.right:
            p = p.right
        p.right = root
        return new_root