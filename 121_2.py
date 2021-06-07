# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 10:54
# @Author  : zxl
# @FileName: 121_2.py



class Solution:
    def maxProfit(self, prices ) -> int:


        min_val = float('inf')
        ans = 0

        for price in prices:

            if price>min_val:
                ans = max(ans,price-min_val)
            min_val = min(min_val,price)
        return ans
