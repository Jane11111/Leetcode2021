# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 22:28
# @Author  : zxl
# @FileName: Offer042_2.py


class Solution:
    def maxSubArray(self, nums ) -> int:

        max_val = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i]+nums[i-1])
            max_val = max(max_val,nums[i])
        return max_val