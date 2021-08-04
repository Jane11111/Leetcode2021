# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 10:32
# @Author  : zxl
# @FileName: 714_3.py

class Solution:
    def maxProfit(self, prices,  fee: int) -> int:

        n = len(prices)
        if n<=1:
            return 0

        buy = -prices[0]-fee
        sell = 0

        for i in range(1,n):

            buy = max(sell-prices[i]-fee,buy)
            sell = max(sell,buy+prices[i])
        return sell


