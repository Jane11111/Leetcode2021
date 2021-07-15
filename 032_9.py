# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 11:39
# @Author  : zxl
# @FileName: 032_9.py



class Solution:
    def longestValidParentheses(self, s: str) -> int:


        dp = [0 for i in range(len(s))]

        ans = 0

        for i in range(len(s)):

            if s[i] == ')':

                if i-1>=0 and s[i-1] == '(':
                    dp[i] = 2+(dp[i-2 ]if i-2>=0 else 0)
                elif i-1>=0 and s[i-1] == ')':
                    if i-1-dp[i-1] >=0 and s[i-1-dp[i-1]] == '(':
                        dp[i] = dp[i-1]+2
                        if i-1-dp[i-1]-1>=0:
                            dp[i]+=dp[i-1-dp[i-1]-1]
            ans = max(ans,dp[i])
        return ans


