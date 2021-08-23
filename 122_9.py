# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 10:34
# @Author  : zxl
# @FileName: 122_9.py



class Solution:
    def maxProfit(self, prices ) -> int:

        buy = -prices[0]
        sell = 0
        for i in range(1,len(prices)):
            buy = max(sell-prices[i],buy)
            sell = max(buy+prices[i],sell)
        return sell