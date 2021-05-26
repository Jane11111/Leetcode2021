# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 11:04
# @Author  : zxl
# @FileName: 005_2.py



class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return s

        ans = s[0]
        n = len(s)
        dp = []
        for  i in range(n):
            dp.append([False for i in range(n)])
            dp[i][i] = True


        for l in range(2,n+1):
            for i in range(n):
                j = i+l-1
                if j>=n:
                    break
                if s[i] == s[j]:
                    dp[i][j] = True if j-i==1 or dp[i+1][j-1] else False
                    if dp[i][j] and j-i+1>len(ans):
                        ans = s[i:j+1]
        return ans

