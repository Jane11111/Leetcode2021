# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 09:28
# @Author  : zxl
# @FileName: 123_5.py


class Solution:
    def maxProfit(self, prices ) -> int:


        n = len(prices)

        if n<=1:
            return 0

        dp0 = -prices[0]
        dp1 = 0
        dp2 = -prices[0]
        dp3 = 0

        for i in range(n):

            dp0 = max(dp0,-prices[i])
            dp1 = max(dp1,dp0+prices[i])
            dp2 = max(dp2,dp1-prices[i])
            dp3 = max(dp3,dp2+prices[i])
        return max(dp1,dp3)





