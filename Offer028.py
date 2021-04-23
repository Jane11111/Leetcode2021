# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 13:10
# @Author  : zxl
# @FileName: Offer028.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:



    def isSymmetric(self, root: TreeNode) -> bool:

        Q = [root]

        while len(Q)>0:

            n = len(Q)
            i = 0
            j = n-1
            while i<j:
                if (Q[i] == None and Q[j] == None) or(Q[i]!=None and Q[j]!=None and Q[i].val == Q[j].val):
                    i+=1
                    j-=1
                else:
                    return False
            i = 0
            while i<n:
                i += 1
                p = Q.pop(0)
                if not p :
                    continue
                Q.append(p.left)
                Q.append(p.right)

        return True



