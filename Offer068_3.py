# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 14:57
# @Author  : zxl
# @FileName: 068_3.py




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        if root.val>max(p.val,q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val< min(p.val,q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        return root






