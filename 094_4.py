# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:32
# @Author  : zxl
# @FileName: 094_4.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:



    def inorderTraversal(self, root: TreeNode):

        if not root:
            return []


        l1 = self.inorderTraversal(root.left)
        l1.append(root.val)
        l2 = self.inorderTraversal(root.right)
        l1.extend(l2)
        return l1