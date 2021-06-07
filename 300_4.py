# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 09:14
# @Author  : zxl
# @FileName: 300_4.py



class Solution:
    def lengthOfLIS(self, nums ) -> int:


        n = len(nums)
        dp = [1 for i in range(n)]

        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i] :
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

