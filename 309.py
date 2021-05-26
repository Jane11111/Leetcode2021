# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 16:34
# @Author  : zxl
# @FileName: 309.py




class Solution:
    def maxProfit(self, prices ) -> int:

        dp0 = [0,0]
        dp1 = -prices[0]
        for i in range(1,len(prices)):
            dp1 = max(dp0[0]-prices[i],dp1)
            dp0[0] = max(dp0[0],dp0[1])
            dp0[1] = max(dp0[0], dp1+prices[i])
        return max(dp0)



