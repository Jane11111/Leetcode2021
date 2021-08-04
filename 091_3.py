# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 15:23
# @Author  : zxl
# @FileName: 091_3.py


class Solution:

    def numDecodings(self, s: str) -> int:

        n = len(s)
        if s[0] == '0':
            return 0
        if n == 1:
            return 1

        dp = [1 for i in range(n+1)]

        for i in range(2,n+1):
            if s[i-1] == '0':
                n1 = 0
            else:
                n1 = dp[i-1]

            if s[i-2] == '0' or s[i-2:i]>'26':
                n2 = 0
            else:
                n2 = dp[i-2]
            dp[i] = n1+n2
        return dp[-1]




