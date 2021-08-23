# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 16:17
# @Author  : zxl
# @FileName: 099_4.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorder(self,root,lst):
        if not root:
            return

        self.inorder(root.left,lst)
        lst.append(root)
        self.inorder(root.right,lst)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        lst = []
        self.inorder(root,lst)

        i = 0
        p1 = None
        while i<len(lst):
            if lst[i].val>lst[i+1].val:
                p1 = lst[i]
                break
            i+=1
        p2 = None
        j = len(lst)-1
        while j>=0:
            if lst[j].val<lst[j-1].val:
                p2 = lst[j]
                break
            j-=1
        p1.val,p2.val = p2.val,p1.val





