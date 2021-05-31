# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 16:02
# @Author  : zxl
# @FileName: 094_6.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorder(self,root,lst):
        if root == None:
            return
        self.inorder(root.left,lst)
        lst.append(root.val)
        self.inorder(root.right,lst)

    def inorderTraversal(self, root: TreeNode):

        lst = []
        self.inorder(root,lst)
        return lst