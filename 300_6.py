# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 22:00
# @Author  : zxl
# @FileName: 300_6.py


class Solution:
    def lengthOfLIS(self, nums ) -> int:


        dp = [1 for i in range(len(nums))]


        for i in range(len(nums)):
            for j in range(i):

                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)


