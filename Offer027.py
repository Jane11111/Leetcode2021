# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 13:07
# @Author  : zxl
# @FileName: Offer027.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        if root == None:
            return root

        p1 = root.left
        p2 = root.right
        root.left = self.mirrorTree(p2)
        root.right = self.mirrorTree(p1)
        return root
