# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 16:30
# @Author  : zxl
# @FileName: 044_2.py

class Solution(object):




    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        new_pattern = ''
        for i in range(len(p)):
            if len(new_pattern) == 0:
                new_pattern+=p[i]
            else:
                if p[i] == '*' and p[i-1] == '*':
                    continue
                else:
                    new_pattern += p[i]

        p = new_pattern
        m = len(s)
        n = len(p)

        dp = []
        for i in range(m+1):
            arr = [False for j in range(n+1)]
            dp.append(arr)
        dp[0][0] = True
        for k in range(n):
            if p[k] == '*':
                dp[0][k+1] = True
            else:
                break

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    # f = False
                    # for k in range(i+1):
                    #     if dp[k][j-1] :
                    #         f = True
                    #         break
                    #
                    # dp[i][j] = f
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] == s[i-1]
        return dp[-1][-1]




obj = Solution()
s = "acdcb"
p = "a*c*b"
f = obj.isMatch(s,p)
print(f)
