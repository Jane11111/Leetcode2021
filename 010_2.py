# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 17:38
# @Author  : zxl
# @FileName: 010_2.py


class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)
        dp = []
        for i in range(m+1):
            dp.append([False for j in range(n+1)])
        dp[m][n] = True
        j = n-1
        while j>=0:
            if p[j] == '*':
                dp[m][j] = dp[m][j+1]
            else:
                if j+1<n and p[j+1] == '*':
                    dp[m][j] = dp[m][j+1]
            j-=1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if p[j] == '*':
                    dp[i][j] = dp[i][j+1]
                elif j+1<n and p[j+1] == '*':
                    if s[i] == p[j] or p[j] == '.':
                        dp[i][j] = dp[i][j+2] or dp[i+1][j+2] or dp[i+1][j]
                    else:
                        dp[i][j] = dp[i][j+2]
                else:
                    if s[i] == p[j] or p[j] == '.':
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = False
        return dp[0][0]


obj = Solution()
s = "mississippi"
p = "mis*is*p*."
ans = obj.isMatch(s,p)
print(ans)



