# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 21:19
# @Author  : zxl
# @FileName: Offer007.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) == 0:
            return None
        val = preorder[0]
        root = TreeNode(val)
        l1 = []
        l2 = []
        for i in range(len(inorder)):
            if inorder[i] == val:
                l1 = inorder[:i]
                l2 = inorder[i+1:]
                break
        left = self.buildTree(preorder[1:1+len(l1)],l1)
        right = self.buildTree(preorder[1+len(l1):],l2)
        root.left = left
        root.right = right
        return root





