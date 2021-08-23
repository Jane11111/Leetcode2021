# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 11:12
# @Author  : zxl
# @FileName: 188_3.py



class Solution:
    def maxProfit(self, k: int, prices ) -> int:

        if len(prices) == 0 or k == 0:
            return 0


        buy = [-prices[0] for i in range(k)]
        sell = [0 for i in range(k)]

        for i in range(1,len(prices)):

            for j in range(k):

                buy[j] = max(buy[j],0-prices[i] if j == 0 else sell[j-1]-prices[i])
                sell[j] = max(sell[j],buy[j]+prices[i])
        return sell[-1]

