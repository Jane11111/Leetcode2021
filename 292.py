# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 22:39
# @Author  : zxl
# @FileName: 292.py

class Solution:
    def canWinNim(self, n: int) -> bool:
        dp = [True for i in range(n+1)]

        for i in range(4,n+1):
            dp[i] = not(dp[i-1] and dp[i-2] and dp[i-3])
        return dp[n]







