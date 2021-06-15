# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 11:01
# @Author  : zxl
# @FileName: 279_2.py


import numpy as np
class Solution:
    def numSquares(self, n: int) -> int:


        nums = [i*i for i in range(1,int(np.sqrt(n))+1)]


        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        for num in nums:
            for v in range(max(1,num),n+1):
                dp[v] = min(dp[v],dp[v-num]+1)
        return dp[n]

obj = Solution()
n = 13
ans = obj.numSquares(n)
print(ans)