# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 21:45
# @Author  : zxl
# @FileName: 897.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return root
        if root.left == None:
            root.right = self.increasingBST(root.right)
            return root
        new_root = self.increasingBST(root.left)
        root.right = self.increasingBST(root.right)

        p = new_root
        while p.right:
            p = p.right
        p.right = root
        root.left = None #记得这一步，要把左边设置为None，不然会出现环
        return new_root
