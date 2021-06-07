# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 10:51
# @Author  : zxl
# @FileName: 005_4.py



class Solution:
    def longestPalindrome(self, s: str) -> str:


        n = len(s)
        dp = []
        for i in range(n):
            dp.append([False for j in range(n)])
            dp[i][i] = True
        max_len = 1
        ans = s[0]
        for l in range(2,n+1):
            for i in range(n):
                j = i+l-1
                if j>=n:
                    break
                if s[i] == s[j] and (i+1>=j-1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if dp[i][j] and j-i+1>max_len:
                        ans = s[i:j+1]
        return ans


