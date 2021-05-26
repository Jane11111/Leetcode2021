# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 14:53
# @Author  : zxl
# @FileName: 122_4.py




class Solution:
    def maxProfit(self, prices ) -> int:


        dp0 = 0
        dp1 = -prices[0]


        for i in range(1,len(prices)):

            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,dp0-prices[i])



        return dp0