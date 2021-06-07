# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 12:25
# @Author  : zxl
# @FileName: 493_4.py




class Solution:
    def findTargetSumWays(self, nums , target: int) -> int:

        dp = []
        sum_val = sum(nums)

        for i in range(len(nums)):
            dp.append([0 for j in range(2 * (sum_val + 1))])

        dp[0][sum_val + nums[0]] += 1
        dp[0][sum_val - nums[0]] += 1

        for i in range(1, len(nums)):
            num = nums[i]
            for v in range(-sum_val,sum_val+1,1):
                if dp[i-1][v+sum_val] >0:
                    dp[i][v+num+sum_val] += dp[i-1][v+sum_val]
                    dp[i][v-num+sum_val] += dp[i-1][v+sum_val]

        ans = 0
        if sum_val + target < 2 * (sum_val + 1) and sum_val + target >= 0:
            ans = dp[len(nums) - 1][sum_val + target]
        return ans

