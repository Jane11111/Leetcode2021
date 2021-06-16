# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 22:31
# @Author  : zxl
# @FileName: 368.py


class Solution:
    def largestDivisibleSubset(self, nums ) :

        dp = [1 for i in range(len(nums))]

        nums.sort()

        for i in range(1,len(nums)):

            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)

        ans = []
        v = max(dp)
        last_num = -1

        for i in range(len(nums)):
            if dp[i] == v:
                last_num = nums[i]

        for i in range(len(nums)-1,-1,-1):
            if dp[i] == v and last_num%nums[i] == 0:
                ans.insert(0,nums[i])
                v-=1
                last_num = nums[i]
        return ans


