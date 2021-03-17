# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 15:01
# @Author  : zxl
# @FileName: 116.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 0:
            return None

        head = TreeNode(postorder[-1])
        idx = 0
        while inorder[idx]!=postorder[-1]:
            idx += 1

        head.left = self.buildTree(inorder[0:idx],postorder[0:idx])
        head.right = self.buildTree(inorder[1+idx:],postorder[idx:-1])
        return head
