# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 16:44
# @Author  : zxl
# @FileName: 005_5.py



class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = []
        for i in range(n):
            dp.append([True for j in range(n)])

        ans = s[0]
        for l in range(2,n+1):
            for i in range(n):
                j = i+l-1
                if j>=n:
                    break
                dp[i][j] = s[i] == s[j] and (j-i<=2 or dp[i+1][j-1])
                if dp[i][j] and j-i+1>len(ans):
                    ans = s[i:j+1]
        return ans

