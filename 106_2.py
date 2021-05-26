# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 15:15
# @Author  : zxl
# @FileName: 106_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder , postorder ) -> TreeNode:

        if len(inorder)==0:
            return None
        if len(inorder) == 1:
            p = TreeNode(inorder[0])
            return p




        root = TreeNode(postorder[-1])

        i = 0
        while i<len(inorder) and inorder[i] != postorder[-1]:
            i+=1

        left = self.buildTree(inorder[:i],postorder[:i])
        right = self.buildTree(inorder[i+1:],postorder[i:-1])
        root.left = left
        root.right = right

        return root



