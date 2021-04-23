# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 21:07
# @Author  : zxl
# @FileName: 214.py


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return s

        n = len(s)
        dp = []
        for i in range(n):
            dp.append([False for i in range(n)])
            dp[i][i] = True
        # i = 0
        for l in range(2,n+1):
            for i in range(0,n-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if j-i>1 else True

                else:
                    dp[i][j] = False
        j = 0
        for i in range(n-1,-1,-1):
            if dp[0][i] == True:
                j = i
                break
        new_s = ''
        for k in range(j+1,n):
            new_s = s[k]+new_s
        return new_s+s

obj = Solution()
s = "abcd"
ans = obj.shortestPalindrome(s)
print(ans)

