# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:30
# @Author  : zxl
# @FileName: 094_3.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recursiveTraversal(self,root,lst):

        if root == None:
            return
        self.recursiveTraversal(root.left,lst)
        lst.append(root.val)
        self.recursiveTraversal(root.right,lst)
        return

    def inorderTraversal(self, root: TreeNode):

        lst = []
        self.recursiveTraversal(root,lst)
        return lst

