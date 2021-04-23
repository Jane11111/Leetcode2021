# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 22:25
# @Author  : zxl
# @FileName: 222_2.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:


        if root == None:
            return 0

        l = 0
        p = root
        while p:
            l+=1
            p = p.left
        r = 0
        p = root
        while p:
            r+=1
            p = p.right
        if l == r:
            return 2**l-1

        return 1+self.countNodes(root.left)+self.countNodes(root.right)