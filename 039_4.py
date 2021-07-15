# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 16:11
# @Author  : zxl
# @FileName: 039_4.py


class Solution:



    def recurSolve(self,nums,idx,sum_val,target,lst,ans):


        if sum_val == target:
            ans.append([item for item in lst])

        if sum_val>target:
            return

        for i in range(idx,len(nums)):

            lst.append(nums[i])
            self.recurSolve(nums,i,sum_val+nums[i],target,lst,ans)
            lst.pop()


    def combinationSum(self, candidates , target: int) :

        ans = []
        lst = []
        self.recurSolve(candidates,0,0,target,lst,ans)
        return ans







