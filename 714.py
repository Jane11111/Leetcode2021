# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 11:04
# @Author  : zxl
# @FileName: 714.py



class Solution:
    def maxProfit(self, prices , fee: int) -> int:

        dp0 = 0
        dp1 = -prices[0]

        for i in range(1,len(prices)):
            dp0 = max(dp0,dp1+prices[i] -fee)
            dp1 = max(dp1,dp0-prices[i])

        return dp0










