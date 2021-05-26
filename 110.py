# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 20:27
# @Author  : zxl
# @FileName: 110.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def height(self,root):
        if root == None:
            return 0,True
        l,fl = self.height(root.left)
        r,fr = self.height(root.right)
        return 1+max(l,r), fl and fr and abs(l-r) == 1

    def isBalanced(self, root: TreeNode) -> bool:

        if root == None:
            return True

        l,fl = self.isBalanced(root.left)
        r,fr = self.isBalanced(root.right)

        return fl and fr and abs(l-r) == 1


