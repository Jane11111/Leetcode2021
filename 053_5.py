# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 11:05
# @Author  : zxl
# @FileName: 053_5.py

# dp O(N)

class Solution:
    def maxSubArray(self, nums ) -> int:

        dp = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):

            dp = max(dp+nums[i],nums[i])
            ans = max(ans,dp)
        return ans


