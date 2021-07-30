# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 14:44
# @Author  : zxl
# @FileName: 199_2.py



class Solution:
    def rob(self, nums ) -> int:

        n = len(nums)
        if n<1:
            return 0


        dp0 = [0 for i in range(n)]
        dp1 = [0 for i in range(n)]

        dp2 = [0 for i in range(n)]
        dp3 = [0 for i in range(n)]
        dp3[0] = nums[0]

        for i in range(1,n):

            dp0[i] = max(dp0[i-1],dp1[i-1])
            dp1[i] = max(dp1[i-1],dp0[i-1]+nums[i])

            dp2[i] = max(dp2[i-1],dp3[i-1])

            if i!=n-1:
                dp3[i] = max(dp2[i-1]+nums[i],dp3[i-1])
            else:
                dp3[i] = dp3[i-1]

        return max(dp1[-1],dp3[-1])



