# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 14:59
# @Author  : zxl
# @FileName: 032_5.py



class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if len(s) == 0:
            return 0

        dp = [0 for i in range(len(s))]

        for i in range(len(s)):
            if s[i] == ')':
                if i-1<0:
                    continue
                if s[i-1] == '(':
                    dp[i] = 2 + (0 if i-2<0 else dp[i-2])
                else:
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1]+2
                        if i-dp[i-1]-1-1>=0:
                            dp[i]+=dp[i-dp[i-1]-2]
                    else:
                        dp[i] = 0
        return max(dp )

