# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 11:51
# @Author  : zxl
# @FileName: 337_3.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def recRob(self,root,can_rob,dic):

        if not root:
            return False

        if root in dic and can_rob in dic[root]:
            return dic[root][can_rob]
        if root not in dic:
            dic[root] = {}

        if not can_rob:

            n1 = self.recRob(root.left,True,dic)
            n2 = self.recRob(root.right,True,dic)
            dic[root][can_rob] = n1+n2
            return n1+n2
        else:

            n1 = self.recRob(root.left,True,dic)
            n2 = self.recRob(root.right,True,dic)

            n3 = self.recRob(root.left,False,dic)
            n4 = self.recRob(root.right,False,dic)

            dic[root][can_rob] = max(n1+n2,n3+n4+root.val)
            return max(n1+n2,n3+n4+root.val)

    def rob(self, root: TreeNode) -> int:

        return self.recRob(root,True,{})