# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 21:54
# @Author  : zxl
# @FileName: 098.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveJudge(self,root, num1,num2):
        if root == None:
            return True

        if root.val <= num1 or root.val >= num2:
            return False

        r1 = self.recursiveJudge(root.left,num1,min(num2,root.val))
        r2 = self.recursiveJudge(root.right,max(num1,root.val),num2)
        if r1 and r2:
            return True
        return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.recursiveJudge(root.left,-2.**32,root.val) and self.recursiveJudge(root.right,root.val,2.**32)

