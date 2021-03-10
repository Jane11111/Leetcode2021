# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 11:17
# @Author  : zxl
# @FileName: 122.py


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        res = 0
        if len(prices) <= 1:
            return 0

        prices.append(0)
        l = 0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                res += (prices[i-1] - prices[l])
                l = i
        return res

obj = Solution()
nums = [7,1,5,3,6,4]
res = obj.maxProfit(nums)
print(res)