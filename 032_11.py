# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 16:05
# @Author  : zxl
# @FileName: 032_11.py

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if len(s) == 0:
            return 0

        st = []
        dp = [-1 for i in range(len(s))]

        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                if len(st):
                    dp[i] = st.pop()

        ans = 0
        i = len(s)-1
        while i>=0:

            if dp[i] == -1:
                i-=1
                continue
            j = dp[i]-1
            while j>=0 and dp[j] !=-1:
                j = dp[j]-1
            if j<0:
                ans = max(i+1,ans)
            else:
                ans = max(i-j,ans)
            i = j
        return ans




