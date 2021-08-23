# -*- coding: utf-8 -*-
# @Time    : 2021-08-17 16:43
# @Author  : zxl
# @FileName: NC92.py


class Solution:
    def LCS(self, s1, s2):
        # write code here

        m = len(s1)
        n = len(s2)

        dp = []
        for i in range(m + 1):
            dp.append([0 for j in range(n + 1)])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        if dp[m][n] == 0:
            return -1
        # for i in range(m + 1):
        #     print(dp[i])
        i = m
        j = n
        s = ''
        while i > 0 and j > 0:

            # if dp[i - 1][j] == dp[i][j]:
            #     i -= 1
            # elif dp[i][j - 1] == dp[i][j]:
            #     j -= 1
            # else:
            #     s = s1[i - 1] + s
            #     i -= 1
            #     j -= 1
            if dp[i - 1] == dp[i]:
                i -= 1
            elif dp[j - 1] == dp[j]:
                j -= 1
            else:
                s = s1[i - 1] + s
                i -= 1
                j -= 1
        return s

obj = Solution()
s1 = "1A2C3D4B56"
s2 = "B1D23A456A"
ans = obj.LCS(s1,s2)
print(ans)