# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 14:03
# @Author  : zxl
# @FileName: Offer068.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':



        if root == None or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        if l and r:
            return root
        if not l :
            return r
        elif not r:
            return l

