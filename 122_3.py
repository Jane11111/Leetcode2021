# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 14:39
# @Author  : zxl
# @FileName: 122_3.py



class Solution:
    def maxProfit(self, prices ) -> int:


        dp0 = [0 for i in range(len(prices))]
        dp1 = [0 for i in range(len(prices))]

        dp1[0] = -prices[0]

        for i in range(1,len(prices)):

            dp0[i] = max(dp0[i-1],dp1[i-1]+prices[i])
            dp1[i] = max(dp0[i-1]-prices[i],dp1[i-1])

        return dp0[len(prices)-1]




