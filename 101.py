# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 10:25
# @Author  : zxl
# @FileName: 101.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        lst = [root]
        while len(lst)>0:

            i = 0
            j = len(lst)-1
            n = len(lst)-1
            for k in range(i,j+1):
                if k<n-k:
                    if (lst[k] ==None and lst[n-k]!=None) or \
                            (lst[k]!=None and lst[n-k] == None) or \
                            (lst[k]!=None and lst[n-k]!=None and lst[k].val!=lst[n-k].val):
                        return False
                if lst[k] == None:
                    continue
                lst.append(lst[k].left)
                lst.append(lst[k].right)
            while i<=j:
                lst.pop(0)
                i+=1
        return True






