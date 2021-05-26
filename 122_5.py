# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 11:10
# @Author  : zxl
# @FileName: 122_5.py



class Solution:
    def maxProfit(self, prices ) -> int:

        if len(prices) == 0:
            return 0


        dp0 = 0
        dp1 = -prices[0]
        for i in range(len(prices)):
            p = prices[i]
            dp0 = max(dp0,dp1+p)
            dp1 = max(dp0-p,dp1)
        return dp0