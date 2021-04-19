# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 22:12
# @Author  : zxl
# @FileName: 097.py


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)

        dp = []
        for i in range(m+1):
            dp.append([False for j in range(n+1)])

        dp[0][0] = True
        for i in range(m):
            if s1[i] == s3[i]:
                dp[i+1][0] = dp[i][0]
        for j in range(n):
            if s2[j] == s3[j]:
                dp[0][j+1] = dp[0][j]

        for i in range(m):
            for j in range(n):
                if s3[i+j+1] != s1[i] and s3[i+j+1] != s2[j]:
                    dp[i+1][j+1] = False
                elif s3[i+j+1] != s1[i] and s3[i+j+1] == s2[j]:
                    dp[i+1][j+1] = dp[i+1][j]
                elif s3[i+j+1] == s1[i] and s3[i+j+1] != s2[j]:
                    dp[i+1][j+1] = dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
        return dp[m][n]

obj = Solution()
s1 = "db"
s2 = "b"
s3 = "cbb"
ans = obj.isInterleave(s1,s2,s3)
print(ans)


