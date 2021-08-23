# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 10:25
# @Author  : zxl
# @FileName: 121_5.py



class Solution:
    def maxProfit(self, prices ) -> int:


        buy = -prices[0]
        sell = 0
        for i in range(1,len(prices)):

            buy = max(buy, -prices[i])
            sell = max(buy+prices[i],sell)
        return sell