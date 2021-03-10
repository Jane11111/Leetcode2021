# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 20:00
# @Author  : zxl
# @FileName: 1379.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def recursiveFind(self,head,target):
        if head == None :
            return head
        if head.val == target:
            return head
        else:
            l = self.recursiveFind(head.left,target)
            r = self.recursiveFind(head.right,target)
            if l:
                return l
            if r:
                return r
            return None

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        res = self.recursiveFind(cloned,target.val)
        return res
