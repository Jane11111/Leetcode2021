# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 10:16
# @Author  : zxl
# @FileName: 070.py

class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0 for i in range(max(n+1,3))]
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

obj = Solution()
n = 2
ans = obj.climbStairs(n)
print(ans)

