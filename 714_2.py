# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 15:15
# @Author  : zxl
# @FileName: 714_2.py



class Solution:
    def maxProfit(self, prices , fee: int) -> int:

        buy = prices[0] + fee

        ans = 0

        for i in range(1,len(prices)):


            if prices[i]+fee<buy:
                buy = prices[i]+fee
            elif prices[i] > buy:
                ans+= prices[i] - buy
                buy = prices[i]
        return ans



