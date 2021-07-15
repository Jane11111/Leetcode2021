# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 16:49
# @Author  : zxl
# @FileName: 040_4.py



class Solution:

    def recurSolve(self,nums,idx,sum_val,target,lst ,ans):

        if sum_val == target:
            ans.append([item for item in lst])
            return
        if sum_val>target or idx>=len(nums):
            return

        i = idx
        while i<len(nums):

            lst.append(nums[i])
            self.recurSolve(nums,i+1,sum_val+nums[i],target,lst,ans)
            lst.pop()

            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1





    def combinationSum2(self, candidates, target: int):

        candidates.sort()

        lst = []
        ans = []
        self.recurSolve(candidates,0,0,target,lst,ans)
        return ans


