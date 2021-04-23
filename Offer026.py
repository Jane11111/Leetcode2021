# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:38
# @Author  : zxl
# @FileName: Offer026.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    def findSameRoot(self,A,B):

        if A==None or B == None:
            return []
        ans = []
        if A.val == B.val:
            ans.append(A)
        l = self.findSameRoot(A.left,B)
        r = self.findSameRoot(A.right,B)
        ans.extend(l)
        ans.extend(r)
        return ans

    def isSame(self,A,B):
        if B == None:
            return True
        if A== None:
            return False

        if A.val != B.val:
            return False
        f1 = self.isSame(A.left,B.left)
        f2 = self.isSame(A.right,B.right)
        return f1 and f2

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if B==None:
            return False

        root_lst = self.findSameRoot(A,B)
        for r in root_lst:
            f = self.isSame(r,B)
            if f:
                return f
        return False


