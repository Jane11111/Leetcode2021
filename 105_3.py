# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 11:25
# @Author  : zxl
# @FileName: 105_3.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder , inorder ) -> TreeNode:

        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        i = 0
        while inorder[i] != preorder[0]:
            i+=1

        left = self.buildTree(preorder[1:1+i],inorder[:i])
        right = self.buildTree(preorder[1+i:],inorder[i+1:])
        root.left = left
        root.right = right
        return root