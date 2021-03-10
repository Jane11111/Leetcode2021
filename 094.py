# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 21:35
# @Author  : zxl
# @FileName: 094.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveTraversal(self,root,lst):
        if root == None:
            return lst

        self.recursiveTraversal(root.left,lst)
        lst.append(root.val)
        self.recursiveTraversal(root.right,lst)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recursiveTraversal(root,res)
        return res


