# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 20:52
# @Author  : zxl
# @FileName: Offer054.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def count(self,root):
        if root == None:
            return 0
        l = self.count(root.left)
        r = self.count(root.right)
        return l+r+1

    def recFind(self,root,k):

        if root == None:
            return 0,0
        cl,val = self.recFind(root.left,k)
        if cl == k-1 :
            return k,root.val
        elif cl>=k:
            return k,val

        cr,val = self.recFind(root.right,k-cl-1)



        return cl+cr+1,val

    def kthLargest(self, root: TreeNode, k: int) -> int:

        n = self.count(root)
        k = n-k+1

        count,val = self.recFind(root,k)
        return val


