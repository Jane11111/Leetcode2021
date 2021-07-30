# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 14:38
# @Author  : zxl
# @FileName: 198_3.py


class Solution:
    def rob(self, nums ) -> int:
        n = len(nums)

        if n <1:
            return 0

        dp0 = [0 for i in range(n)]
        dp1 = [0 for i in range(n)]
        dp1[0] = nums[0]

        for i in range(1,n):

            dp0[i] = max(dp0[i-1],dp1[i-1])
            dp1[i] = max(dp0[i-1]+nums[i],dp1[i-1])
        return dp1[-1]



