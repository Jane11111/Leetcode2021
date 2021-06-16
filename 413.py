# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 14:25
# @Author  : zxl
# @FileName: 413.py


class Solution:
    def numberOfArithmeticSlices(self, nums ) -> int:


        dp = [0 for i in range(len(nums))]

        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1

        return sum(dp)