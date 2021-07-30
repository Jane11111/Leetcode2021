# -*- coding: utf-8 -*-
# @Time    : 2021-07-27 19:35
# @Author  : zxl
# @FileName: 122_6.py



class Solution:
    def maxProfit(self, prices ) -> int:


        ans = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+= prices[i]-prices[i-1]
        return ans