# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 09:55
# @Author  : zxl
# @FileName: 309_2.py

class Solution:
    def maxProfit(self, prices ) -> int:

        n = len(prices)

        buy = [0 for i in range(n)] # 当前手中有一支股票情况下，最大收益
        buy[0] = -prices[0]

        dp0 = [0 for i in range(n)] # 当前无交易
        dp1 = [0 for i in range(n)] # 当前可交易

        for i in range(1,n):

            dp0[i] = max(dp0[i-1],dp1[i-1])

            dp1[i] = max(buy[i-1]+prices[i],dp1[i-1])

            buy[i] = max(buy[i-1],dp0[i-1]-prices[i])


        return dp1[-1]




