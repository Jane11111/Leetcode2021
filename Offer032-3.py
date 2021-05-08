# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 15:12
# @Author  : zxl
# @FileName: Offer032-3.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :

        l2r = True
        ans = []
        Q = [root] if root else []

        while len(Q)>0:

            n = len(Q)
            i = 0
            cur_lst = []

            while i<n:
                p = Q.pop(0)
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
                i+=1
                if l2r:
                    cur_lst.append(p.val)
                else:
                    cur_lst.insert(0,p.val)
            ans.append(cur_lst)
            l2r = not l2r
        return ans
