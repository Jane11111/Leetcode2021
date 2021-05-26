# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 14:34
# @Author  : zxl
# @FileName: 123_2.py


class Solution:
    def maxProfit(self, prices ) -> int:

        if len(prices) == 0:
            return 0

        dp1 = 0
        dp2 = -prices[0]
        dp3 = 0
        dp4 = -prices[0]

        for price in prices:
            dp1 = max(dp1,dp2+price)
            dp2 = max(dp2,-price)
            dp3 = max(dp3,dp4+price)
            dp4 = max(dp4,dp1-price)
        return max(dp1,dp3)
