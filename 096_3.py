# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 15:57
# @Author  : zxl
# @FileName: 096_3.py


class Solution:
    def numTrees(self, n: int) -> int:


        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]

        return dp[n]


