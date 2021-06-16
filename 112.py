# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 21:28
# @Author  : zxl
# @FileName: 112.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recFind(self,root,sum_val,target_val):

        if not root.left and not root.right:
            return sum_val+root.val == target_val

        f1 = False
        f2 = False
        if root.left:
            f1 = self.recFind(root.left,sum_val+root.val,target_val)
        if root.right:
            f2 = self.recFind(root.right,sum_val+root.val,target_val)
        return f1 or f2

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:


        if root == None:
            return False

        return self.recFind(root,0,targetSum)




