# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 19:42
# @Author  : zxl
# @FileName: 145_7.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) :

        if not root:
            return []

        p = root
        lst = []
        ans = []
        while p:
            lst.append(p)
            ans.insert(0,p.val)
            p = p.right

        while len(lst)>0:
            p = lst.pop()
            p = p.left

            while p:
                lst.append(p)
                ans.insert(0,p.val)
                p = p.right
        return ans

