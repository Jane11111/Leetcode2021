# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 20:46
# @Author  : zxl
# @FileName: 010_4.py



class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        n1 = len(p)
        n2 = len(s)
        dp = []
        for i in range(n1+1):
            dp.append([False for j in range(n2+1)])
        dp[0][0] = True
        for i in range(1,n1+1):

            if p[i-1] == '*':
                dp[i] = dp[i-2]

        for i in range(1,n1+1):
            for j in range(1,n2+1):

                if p[i-1] == '*':
                    f1 = dp[i-2][j]
                    f2 = (p[i-2] == s[j-1] or p[i-2] == '.') and dp[i-2][j-1]
                    f3 = (p[i-2] == s[j-1] or p[i-2] == '.') and dp[i][j-1]
                    dp[i][j] = f1 or f2 or f3
                else:

                    dp[i][j] = (p[i-1] == s[j-1] or p[i-1] == '.') and dp[i-1][j-1]
        return dp[n1][n2]


obj = Solution()
s = 'ab'
p = '.*'
ans = obj.isMatch(s,p)
print(ans)





