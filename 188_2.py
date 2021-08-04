# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 09:50
# @Author  : zxl
# @FileName: 188_2.py

class Solution:
    def maxProfit(self, k: int, prices ) -> int:
        n = len(prices)

        if n<=1 or k == 0:
            return 0


        buy = [-prices[0] for i in range(k)]
        sell = [0 for i in range(k)]

        for i in range(1,n):

            for j in range(k):
                buy[j] = max(buy[j],(sell[j-1]-prices[i]) if j>=1 else -prices[i])
                sell[j] = max(sell[j],buy[j]+prices[i])
        return sell[-1]


