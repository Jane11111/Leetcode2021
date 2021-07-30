# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 10:02
# @Author  : zxl
# @FileName: 115_2.py

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)

        dp = []

        for i in range(m+1):
            dp.append([0 for j in range(n+1)])
            dp[i][0] = 1



        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] +  dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]



obj = Solution()
s = "rabbbit"
t = "rabbit"
ans = obj.numDistinct(s,t)
print(ans)