# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 21:32
# @Author  : zxl
# @FileName: 572.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def recursiveFind(self,root,subRoot,f):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False

        if f :
            if root.val!=subRoot.val:
                return False
            f1 = self.recursiveFind(root.left, subRoot.left,f)
            f2 = self.recursiveFind(root.right, subRoot.right,f)
            return f1 and f2
        else:



            if root.val == subRoot.val:
                f1 = self.recursiveFind(root.left,subRoot.left,True)
                f2 = self.recursiveFind(root.right,subRoot.right,True)
                if f1 and f2:
                    return True
            f1 = self.recursiveFind(root.left,subRoot,f)
            f2 = self.recursiveFind(root.right,subRoot,f)
            return f1 or f2

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        return self.recursiveFind(root,subRoot,False)





