# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 15:52
# @Author  : zxl
# @FileName: 095_2.py




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recGen(self,nums ):
        if len(nums) == 0:
            return [None]
        lst = []
        for i in range(len(nums)):

            left_lst = self.recGen(nums[:i])
            right_lst = self.recGen(nums[i+1:])
            for l in left_lst:
                for r in right_lst:
                    root = TreeNode(nums[i])
                    root.left = l
                    root.right = r
                    lst.append(root)
        return lst


    def generateTrees(self, n: int) :

        nums = [i for i in range(1,n+1)]
        ans = self.recGen(nums)
        return ans

