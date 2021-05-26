# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 14:13
# @Author  : zxl
# @FileName: 121.py



class Solution:
    def maxProfit(self, prices ) -> int:

        min_val = prices[0]

        ans = 0

        for i in range(1,len(prices)):
            min_val = min(min_val,prices[i])

            if prices[i]>min_val:
                ans = max(prices[i]-min_val,ans)
        return ans

