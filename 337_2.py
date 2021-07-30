# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 14:53
# @Author  : zxl
# @FileName: 337_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recRob(self,root,f,dic):


        if not root:
            return 0


        if root in dic and f in dic[root]:
            return dic[root][f]
        if root not in dic:
            dic[root] = {}


        if not f:
            n1 = self.recRob(root.left,True,dic)
            n2 = self.recRob(root.right,True,dic)
            return n1+n2

        n1 = self.recRob(root.left,False,dic)
        n2 = self.recRob(root.right,False,dic)

        n3 = self.recRob(root.left,True,dic)
        n4 = self.recRob(root.right,True,dic)

        ans = max(n1+n2+root.val,n3+n4)

        dic[root][f] = ans
        return ans




    def rob(self, root: TreeNode) -> int:

        return self.recRob(root,True,{})


