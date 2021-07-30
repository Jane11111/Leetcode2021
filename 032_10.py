# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 15:55
# @Author  : zxl
# @FileName: 032_10.py

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dp = [0 for i in range(len(s))]

        for i in range(len(s)):
            if s[i] == '(' or i-1<0:
                continue


            if s[i-1] == '(':
                dp[i] = 2+(dp[i-2] if i-2>=0 else 0)
            else:
                if i-1-dp[i-1]>=0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1]+2
                    if i-1-dp[i-1]-1>=0:
                        dp[i]+= dp[i-1-dp[i-1]-1]
        return max(dp)


