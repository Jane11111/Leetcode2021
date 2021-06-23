# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 11:40
# @Author  : zxl
# @FileName: 106_5.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder , postorder ) -> TreeNode:


        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])

        idx = 0
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                idx = i
                break
        l = self.buildTree(inorder[:idx],postorder[:idx])
        r = self.buildTree(inorder[idx+1:],postorder[idx:-1])
        root.left = l
        root.right = r
        return root
