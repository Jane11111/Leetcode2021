# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:01
# @Author  : zxl
# @FileName: 144_4.py



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
        lst.append(root.val)
        self.recursiveTraversal(root.left,lst)
        self.recursiveTraversal(root.right,lst)
        return

    def preorderTraversal(self, root: TreeNode) :

        lst = []
        self.recursiveTraversal(root,lst)
        return lst

