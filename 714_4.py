# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 11:31
# @Author  : zxl
# @FileName: 714_4.py



class Solution:
    def maxProfit(self, prices , fee: int) -> int:


        buy = -prices[0]-fee
        sell = 0

        for i in range(1,len(prices)):

            buy = max(buy,sell-prices[i]-fee)
            sell = max(sell,buy+prices[i])
        return sell