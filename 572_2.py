# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 21:46
# @Author  : zxl
# @FileName: 572_2.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isSametree(self,root,subRoot):
        if root == None and subRoot==None:
            return True
        if root == None or subRoot == None:
            return False
        return root.val == subRoot.val and self.isSametree(root.left,subRoot.left) and self.isSametree(root.right,subRoot.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        if root == None and subRoot==None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            f1 = self.isSametree(root.right,subRoot.right)
            f2 = self.isSametree(root.left,subRoot.left)
            if f1 and f2:
                return True
        f1 = self.isSubtree(root.left,subRoot)
        f2 = self.isSubtree(root.right,subRoot)
        return f1 or f2