# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 21:50
# @Author  : zxl
# @FileName: 053_2.py



class Solution:
    def maxSubArray(self, nums ) -> int:

        sum_val = 0
        min_sum = float('inf')

        ans = float('-inf')

        for num in nums:
            sum_val+=num

            ans = max(ans,sum_val-min_sum,sum_val)
            min_sum = min(min_sum,sum_val)
        return ans
