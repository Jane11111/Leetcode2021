# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 19:39
# @Author  : zxl
# @FileName: 094_8.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) :

        if not root:
            return []

        lst = []
        ans = []
        p = root
        while p:
            lst.append(p)
            p = p.left

        while len(lst)>0:

            p = lst.pop()
            ans.append(p.val)
            p = p.right
            while p:
                lst.append(p)
                p = p.left
        return ans
