# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 15:10
# @Author  : zxl
# @FileName: 437_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def memorizeRec(self,root,targetSum,dic,cur_sum):
        if root == None:
            return 0
        cur_sum+= root.val
        ans = 0
        if cur_sum-targetSum in dic:
            ans += dic[cur_sum-targetSum]
        # if cur_sum == targetSum:
        #     ans+=1

        if cur_sum not in dic:
            dic[cur_sum] = 0
        dic[cur_sum]+=1

        ans += self.memorizeRec(root.left,targetSum,dic,cur_sum)
        ans += self.memorizeRec(root.right,targetSum,dic,cur_sum)

        dic[cur_sum] -=1
        return ans


    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        dic = {}
        dic[0] = 1

        ans = self.memorizeRec(root,targetSum,dic,0)
        return ans









