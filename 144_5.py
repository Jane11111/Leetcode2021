# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:04
# @Author  : zxl
# @FileName: 144_5.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:




    def preorderTraversal(self, root: TreeNode) :

        if root == None:
            return []

        l1 = self.preorderTraversal(root.left)
        l2 = self.preorderTraversal(root.right)
        l1.insert(0,root.val)
        l1.extend(l2)
        return l1

