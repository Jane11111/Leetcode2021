# -*- coding: utf-8 -*-
# @Time    : 2021-07-27 19:32
# @Author  : zxl
# @FileName: 121_3.py


class Solution:
    def maxProfit(self, prices ) -> int:

        ans = 0
        maxval = 0
        for i in range(len(prices)-1,-1,-1):
            maxval = max(maxval,prices[i])
            ans = max(ans,maxval-prices[i])
        return ans



