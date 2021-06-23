# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 10:17
# @Author  : zxl
# @FileName: 105_6.py



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

        idx = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                idx = i
                break

        l = self.buildTree(preorder[1:1+idx],inorder[:idx])
        r = self.buildTree(preorder[1+idx:],inorder[idx+1:])
        root = TreeNode(preorder[0])
        root.left = l
        root.right = r
        return root

