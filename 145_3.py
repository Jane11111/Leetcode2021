# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:42
# @Author  : zxl
# @FileName: 145_3.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) :


        if root == None:
            return []

        l1 = self.postorderTraversal(root.left)
        l2 = self.postorderTraversal(root.right)
        l1.extend(l2)
        l1.append(root.val)
        return l1