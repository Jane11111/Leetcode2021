# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 10:26
# @Author  : zxl
# @FileName: 122_8.py


class Solution:
    def maxProfit(self, prices) -> int:


        n = len(prices)

        if n<=1:
            return 0

        buy = -prices[0]
        sell = 0

        for i in range(1,n):
            buy = max(buy,sell-prices[i])
            sell = max(sell,buy+prices[i])
        return sell

