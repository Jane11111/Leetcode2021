# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:44
# @Author  : zxl
# @FileName: 377_5.py




class Solution:


    def recurSolve(self,nums,sum_val,target,last_val):

        if sum_val == target:
            return 1
        if sum_val > target:
            return 0
        count = 0
        for i in range(len(nums)):

            num = nums[i]
            if num == last_val :
                continue
            for j in range(1,(target-sum_val)//num +2):
                count+= self.recurSolve(nums,sum_val+num*j,target,num)
        return count

    def combinationSum4(self, nums, target: int) -> int:

        ans = self.recurSolve(nums,0,target,-1)
        return ans


