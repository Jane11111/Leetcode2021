# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 11:17
# @Author  : zxl
# @FileName: 309_3.py



class Solution:
    def maxProfit(self, prices ) -> int:



        buy1 = -prices[0]
        sell1 = 0 # 在冷冻期内
        sell2 = 0 # 不在冷冻期内

        for i in range(1,len(prices)):
            old_buy1 = buy1
            buy1 = max(buy1,sell2-prices[i])
            sell2 = max(sell2,sell1)
            sell1 = max(sell1,old_buy1+prices[i])
        return max(sell1,sell2)