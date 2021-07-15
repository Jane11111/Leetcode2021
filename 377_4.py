# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:37
# @Author  : zxl
# @FileName: 377_3.py




class Solution:


    def recurSolve(self,nums, sum_val,target ):

        if sum_val == target:
            return 1
        if sum_val > target:
            return 0
        count = 0
        for i in range( len(nums)):

            count+=self.recurSolve(nums, sum_val+nums[i],target )
        return count


    def combinationSum4(self, nums , target: int) -> int:




        ans = self.recurSolve(nums, 0,target )
        return ans