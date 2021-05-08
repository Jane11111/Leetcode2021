# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 14:36
# @Author  : zxl
# @FileName: Offer063.py


class Solution:
    def maxProfit(self, prices )  :

        if len(prices) == 0:
            return 0

        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<=min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-min_price)
        return max_profit
