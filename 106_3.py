# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 15:21
# @Author  : zxl
# @FileName: 106_3.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def recursiveBuild(self,inorder,postorder,si,ei,sp,ep,dic):


        if si>ei:
            return None
        if si == ei:
            return TreeNode(inorder[si])

        root = TreeNode(postorder[ep])

        idx = dic[postorder[ep]]

        left = self.recursiveBuild(inorder,postorder,si,idx-1,sp,sp+(idx-si)-1,dic)
        right = self.recursiveBuild(inorder,postorder,idx+1,ei,sp+(idx-si),ep-1,dic)
        root.left = left
        root.right = right
        return root



    def buildTree(self, inorder, postorder) -> TreeNode:


        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        root = self.recursiveBuild(inorder,postorder,0,len(inorder)-1,0,len(inorder)-1,dic)
        return root

