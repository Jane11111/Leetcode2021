# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 13:57
# @Author  : zxl
# @FileName: Offer055.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:

    def getHeight(self,root):
        if root == None:
            return 0

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)

        if l== -1 or r == -1 or abs(l-r)>1:
            return -1

        return max(l,r)+1



    def isBalanced(self, root: TreeNode) -> bool:

        h = self.getHeight(root)

        return h!=-1