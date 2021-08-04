# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 10:49
# @Author  : zxl
# @FileName: 087_4.py

class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:

        n = len(s1)

        dp = []
        for i in range(n+1):
            mat = []
            for j in range(n):
                mat.append([True for k in range(n)])
            dp.append(mat)

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        for l in range(2,n+1):

            for i in range(n):
                if i+l-1>=n:
                    break
                for j in range(n):
                    if j+l-1>=n:
                        break

                    f = False
                    for l2 in range(1,l):
                        f1 = dp[l2][i][j]
                        f2 = dp[l-l2][i+l2][j+l2]

                        f3 = dp[l2][i][j+l-l2]
                        f4 = dp[l-l2][i+l2][j]

                        if f1 and f2 or f3 and f4:
                            f = True
                            break
                    dp[l][i][j] = f
        return dp[n][0][0]






