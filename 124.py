# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 17:50
# @Author  : zxl
# @FileName: 124.py



class Solution:
    def maxProfit(self, k: int, prices ) -> int:

        if len(prices) == 0:
            return 0


        dp1 = [-prices[0] for i in range(k)]
        dp0 = [0 for i in range(k)]


        for i in range(1,len(prices)):

            p = prices[i]

            for j in range(k):
                tmp = dp1[j]

                dp1[j] = max(dp1[j],dp0[j-1]-p if j>0 else -p)
                dp0[j] = max(dp0[j],tmp+p  )
        return max(dp0)

obj = Solution()
k = 2
prices = [3,2,6,5,0,3]
ans = obj.maxProfit(k,prices)
print(ans)