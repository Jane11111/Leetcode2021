# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:29
# @Author  : zxl
# @FileName: 040_5.py



class Solution:

    def recurSolve(self,nums,idx,target,sum_val,lst,ans):


        if sum_val == target:
            ans.append([item for item in lst])
            return
        if sum_val > target:
            return

        i = idx
        while i<len(nums):

            lst.append(nums[i])
            self.recurSolve(nums,i+1,target,sum_val+nums[i],lst,ans)
            lst.pop()
            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1




    def combinationSum2(self, candidates , target: int) :

        candidates.sort()
        lst = []
        ans = []
        self.recurSolve(candidates,0,target,0,lst,ans)
        return ans




