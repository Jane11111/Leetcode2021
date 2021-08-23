# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 11:41
# @Author  : zxl
# @FileName: 198_4.py



class Solution:
    def rob(self, nums ) -> int:


        dp0 = 0
        dp1 = nums[0]

        for i in range(1,len(nums)):

            old_dp0 = dp0

            dp0 = max(dp0,dp1)
            dp1 = max(dp1,old_dp0+nums[i])
        return max(dp0,dp1)
