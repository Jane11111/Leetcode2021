# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 09:14
# @Author  : zxl
# @FileName: 123_4.py

class Solution:
    def maxProfit(self, prices ) -> int:

        n = len(prices)

        if n<=1:
            return 0


        dp0 = [0 for i in range(n)]
        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]
        dp3 = [0 for i in range(n)]

        dp0[0] = -prices[0]
        dp2[0] = -prices[0]

        for i in range(1,n):
            dp0[i] = max(dp0[i-1],-prices[i])
            dp1[i] = max(dp1[i-1],dp0[i-1]+prices[i])

            dp2[i] = max(dp2[i-1],dp1[i-1]-prices[i])
            dp3[i] = max(dp3[i-1],dp2[i-1]+prices[i])
        return max(dp1[-1],dp3[-1])





