# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 14:34
# @Author  : zxl
# @FileName: 105.py




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) <= 0:
            return None

        head = TreeNode(preorder[0])

        idx = 0
        while inorder[idx] != preorder[0]:
            idx +=1

        head.left = self.buildTree(preorder[1:1+idx],inorder[:idx])
        head.right = self.buildTree(preorder[1+idx:],inorder[idx+1:])
        return head



