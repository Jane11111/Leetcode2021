# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 14:52
# @Author  : zxl
# @FileName: 437.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recursivePath(self,root,target_num,continued):

        if root == None :
            return 0
        ans = 0
        if root.val == target_num:
            ans+=1
        l1 = self.recursivePath(root.left,target_num-root.val,True)
        l2 = self.recursivePath(root.right,target_num-root.val,True)
        if not continued:
            l1 += self.recursivePath(root.left,target_num,continued)
            l2 += self.recursivePath(root.right,target_num,continued)
        return ans+l1+l2

    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        ans = self.recursivePath(root,targetSum,False)
        return ans