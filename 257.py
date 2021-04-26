# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 21:36
# @Author  : zxl
# @FileName: 257.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def find(self,root,s):
        if root == None:
            return [s]
        if len(s)>0:
            s+='->'
        s+= str(root.val)
        ans = []

        if not root.left and not root.right:
            return [s]

        if root.left:
            ans.extend(self.find(root.left,s))

        if root.right:
            ans.extend(self.find(root.right,s))
        return ans



    def binaryTreePaths(self, root: TreeNode)  :

        ans = self.find(root,'')
        return ans

