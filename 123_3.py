# -*- coding: utf-8 -*-
# @Time    : 2021-07-27 19:36
# @Author  : zxl
# @FileName: 123_3.py



class Solution:
    def maxProfit(self, prices ) -> int:

        if len(prices)<=1:
            return 0

        dp1 = -prices[0]
        dp2 = 0
        dp3 = -prices[0]
        dp4 = 0


        for i in range(1,len(prices)):
            tmp1 = dp1
            dp1 = max(dp1,-prices[i])
            tmp2 = dp2
            dp2 = max(dp2,tmp1+prices[i])
            tmp3 = dp3
            dp3 = max(dp3,tmp2-prices[i])
            dp4 = max(dp4,tmp3+prices[i])
        return max(dp2,dp4)


