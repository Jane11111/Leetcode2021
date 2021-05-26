# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 15:02
# @Author  : zxl
# @FileName: 123.py



class Solution:
    def maxProfit(self, prices ) -> int:



        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for i in range(1,len(prices)):


            tmp1 = buy1
            tmp2 = sell1
            tmp3 = buy2
            tmp4 = sell2

            buy1 = max(tmp1,-prices[i])
            sell1 = max(tmp2,tmp1+prices[i])
            buy2 = max(tmp3,tmp2-prices[i])
            sell2 = max(tmp4,tmp3+prices[i])
        return max(sell1,sell2)

obj = Solution()
prices = [1]
ans = obj.maxProfit(prices)
print(ans)