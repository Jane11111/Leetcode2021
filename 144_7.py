# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 19:37
# @Author  : zxl
# @FileName: 144_7.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode)  :

        if not root :
            return []

        lst = []
        ans = []

        p = root

        while p:
            lst.append(p)
            ans.append(p.val)
            p = p.left

        while len(lst)>0:
            p = lst.pop()
            p = p.right
            while p:
                lst.append(p)
                ans.append(p.val)
                p = p.left
        return ans




