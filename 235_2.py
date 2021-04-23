# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 13:22
# @Author  : zxl
# @FileName: 235_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p,q = q,p


        if root == None:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        if p.val<root.val and q.val>root.val:
            return root
        if q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return self.lowestCommonAncestor(root.right,p,q)

