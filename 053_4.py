# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 10:00
# @Author  : zxl
# @FileName: 053_4.py

class Solution:
    def maxSubArray(self, nums ) -> int:

        nums.insert(0,0)
        min_val = 0
        sum_val = 0
        ans = float('-inf')

        for i in range(1,len(nums)):

            sum_val+=nums[i]
            ans = max(ans,sum_val,sum_val-min_val)
            min_val = min(min_val,sum_val)
        return ans

