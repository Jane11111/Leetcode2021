# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 10:07
# @Author  : zxl
# @FileName: 122_7.py

class Solution:
    def maxProfit(self, prices ) -> int:


        n = len(prices)

        dp = 0
        for i in range(1,n):
            dp = max(dp,dp+prices[i]-prices[i-1])
        return dp

