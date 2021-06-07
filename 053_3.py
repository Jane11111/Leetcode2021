# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 21:54
# @Author  : zxl
# @FileName: 053_3.py




class Solution:
    def maxSubArray(self, nums ) -> int:


        ans = float('-inf')
        sum_val = 0

        p = -1
        for i in range(len(nums)):
            sum_val += nums[i]
            ans = max(ans,sum_val)

            while sum_val<0:
                p+=1
                sum_val-=nums[p]
        return ans
